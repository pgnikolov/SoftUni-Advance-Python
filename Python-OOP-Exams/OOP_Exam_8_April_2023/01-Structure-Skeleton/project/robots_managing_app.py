from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    service_types = {
        'MainService': MainService,
        'SecondaryService': SecondaryService}
    robot_types = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, name):
        if self.check_service_type(service_type):
            service = self.service_types[service_type](name)
            self.services.append(service)
            return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        if self.check_robot_type(robot_type):
            robot = self.robot_types[robot_type](name, kind, price)
            self.robots.append(robot)
            return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.searching_for_robot_by_name(robot_name)
        service = self.searching_for_service_by_name(service_name)

        if (type(robot).__name__ == "MaleRobot" and type(service).__name__ == "SecondaryService") \
                or (type(robot).__name__ == "FemaleRobot" and type(service).__name__ == "MainService"):
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.searching_for_service_by_name(service_name)

        for robot in service.robots:
            if robot.name == robot_name:
                robot_obj = robot
                break
        else:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot_obj)
        self.robots.append(robot_obj)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.searching_for_service_by_name(service_name)
        [robot.eating() for robot in service.robots]
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name):
        service = self.searching_for_service_by_name(service_name)
        total_price = sum([robot.price for robot in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return "\n".join([service.details() for service in self.services])

    def check_service_type(self, service_type):
        if service_type not in self.service_types:
            raise Exception("Invalid service type!")
        return True

    def check_robot_type(self, robot_type):
        if robot_type not in self.robot_types:
            raise Exception("Invalid robot type!")
        return True

    def check_robot_service(self, robot_name, service_name):
        r = [rob for rob in self.robots if rob.name == robot_name][0]
        rtype = r.__class__.__name__
        s = [ser for ser in self.services if ser.name == service_name][0]
        stype = s.__class__.__name__
        if (stype == 'MainService' and rtype == 'MaleRobot') or (
                stype == 'SecondaryService' and rtype == 'FemaleRobot'):
            return True
        return False

    def searching_for_robot_by_name(self, name):
        for robot in self.robots:
            if robot.name == name:
                return robot

    def searching_for_service_by_name(self, name):
        for service in self.services:
            if service.name == name:
                return service
