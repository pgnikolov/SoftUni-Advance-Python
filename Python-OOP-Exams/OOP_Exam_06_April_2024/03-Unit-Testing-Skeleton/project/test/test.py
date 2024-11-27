from project.social_media import SocialMedia
from unittest import TestCase, main


class TestSocialMedia(TestCase):
    def setUp(self):
        self.social_media = SocialMedia(username="test_user", platform="Instagram", followers=100, content_type="text")

    def test_initialization_valid(self):
        sm = SocialMedia(username="user123", platform="YouTube", followers=200, content_type="video")
        self.assertEqual(sm._username, "user123")
        self.assertEqual(sm.platform, "YouTube")
        self.assertEqual(sm.followers, 200)
        self.assertEqual(sm._content_type, "video")

    def test_initialization_invalid_platform(self):
        with self.assertRaises(ValueError):
            SocialMedia(username="user123", platform="LinkedIn", followers=200, content_type="video")

    def test_get_platform(self):
        self.assertEqual(self.social_media.platform, "Instagram")

    def test_set_valid_platform(self):
        self.social_media.platform = "Twitter"
        self.assertEqual(self.social_media.platform, "Twitter")

    def test_set_invalid_platform(self):
        with self.assertRaises(ValueError):
            self.social_media.platform = "LinkedIn"

    def test_get_followers(self):
        self.assertEqual(self.social_media.followers, 100)

    def test_set_valid_followers(self):
        self.social_media.followers = 150
        self.assertEqual(self.social_media.followers, 150)

    def test_set_invalid_followers(self):
        with self.assertRaises(ValueError):
            self.social_media.followers = -10

    def test_create_post(self):
        response = self.social_media.create_post("This is a new post")
        self.assertEqual(response, "New text post created by test_user on Instagram.")
        self.assertEqual(len(self.social_media._posts), 1)
        self.assertEqual(self.social_media._posts[0]['content'], "This is a new post")

    # Test Like Post
    def test_like_post_valid(self):
        self.social_media.create_post("This is a new post")
        response = self.social_media.like_post(0)
        self.assertEqual(response, "Post liked by test_user.")
        self.assertEqual(self.social_media._posts[0]['likes'], 1)

    def test_like_post_invalid_index(self):
        response = self.social_media.like_post(5)
        self.assertEqual(response, "Invalid post index.")

    def test_like_post_max_likes(self):
        self.social_media.create_post("This is a new post")
        self.social_media._posts[0]['likes'] = 10
        response = self.social_media.like_post(0)
        self.assertEqual(response, "Post has reached the maximum number of likes.")

    # Test Comment on Post
    def test_comment_on_post_valid(self):
        self.social_media.create_post("This is a new post")
        response = self.social_media.comment_on_post(0, "This is a valid comment!")
        self.assertEqual(response, "Comment added by test_user on the post.")
        self.assertEqual(len(self.social_media._posts[0]['comments']), 1)

    def test_comment_on_post_short_comment(self):
        self.social_media.create_post("This is a new post")
        response = self.social_media.comment_on_post(0, "Short")
        self.assertEqual(response, "Comment should be more than 10 characters.")

    def test_comment_on_post_invalid_index(self):
        with self.assertRaises(IndexError):
            self.social_media.comment_on_post(5, "This is a valid comment!")


if __name__ == "__main__":
    main()