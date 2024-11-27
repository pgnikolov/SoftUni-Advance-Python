from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    INFLUENCER_TYPES = {'PremiumInfluencer': PremiumInfluencer, 'StandardInfluencer': StandardInfluencer}
    CAMPAIGN_TYPES = {'LowBudgetCampaign': LowBudgetCampaign, 'HighBudgetCampaign': HighBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.INFLUENCER_TYPES.keys():
            return f"{influencer_type} is not an allowed influencer type."

        if self._get_influencer(username):
            return f"{username} is already registered."

        new_influencer = self.INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.CAMPAIGN_TYPES.keys():
            return f"{campaign_type} is not a valid campaign type."

        for el in self.campaigns:
            if el.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        inf = self._get_influencer(influencer_username)
        if inf is None:
            return f"Influencer '{influencer_username}' not found."

        camp = self._get_campaign(campaign_id)
        if camp is None:
            return f"Campaign with ID {campaign_id} not found."

        if not camp.check_eligibility(inf.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = inf.calculate_payment(camp)
        if payment > 0.0:
            camp.approved_influencers.append(inf)
            camp.budget -= payment
            inf.campaigns_participated.append(camp)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_camp_followers = {}
        for camp in self.campaigns:
            total_followers = 0
            for influencer in camp.approved_influencers:
                campaign_type = type(camp).__name__
                reached = influencer.reached_followers(campaign_type)
                total_followers += reached
            if total_followers > 0:
                total_camp_followers[camp] = total_followers

        return total_camp_followers


    def influencer_campaign_report(self, username: str):
        inf = self._get_influencer(username)
        result = inf.display_campaigns_participated()
        return result

    def campaign_statistics(self):
        total_reached_followers = self.calculate_total_reached_followers()
        campaign_details = []
        for camp in self.campaigns:
            total_influencers = len(camp.approved_influencers)
            total_budget = camp.budget
            reached_followers = total_reached_followers.get(camp, 0)
            campaign_details.append((camp, total_influencers, total_budget, reached_followers))

        campaign_details.sort(key=lambda x: (x[1], -x[2]))

        statistics = "$$ Campaign Statistics $$\n"
        for camp, total_influencers, total_budget, reached_followers in campaign_details:
            statistics += f"  * Brand: {camp.brand}, Total influencers: {total_influencers}, "
            statistics += f"Total budget: ${total_budget:.2f}, Total reached followers: {reached_followers}\n"

        return statistics

    def _get_influencer(self, name):
        for el in self.influencers:
            if el.username == name:
                return el

    def _get_campaign(self, cam_id):
        for el in self.campaigns:
            if el.campaign_id == cam_id:
                return el
