from django.conf import settings
import mailchimp_marketing
from mailchimp_marketing.api_client import ApiClientError
from typing import Dict, Any

class MailchimpService:
    def __init__(self):
        self.client = mailchimp_marketing.Client()
        self.client.set_config({
            "api_key": settings.MAILCHIMP_API_KEY,
            "server": settings.MAILCHIMP_REGION
        })
        self.audience_id = settings.MAILCHIMP_AUDIENCE_ID

    def add_subscriber(self, email: str, status: str = "subscribed", merge_fields: Dict[str, Any] = None) -> bool:
        """
        Add a new subscriber to the Mailchimp audience list
        """
        try:
            member_info = {
                "email_address": email,
                "status": status,
            }
            if merge_fields:
                member_info["merge_fields"] = merge_fields

            self.client.lists.add_list_member(
                self.audience_id,
                member_info
            )
            return True
        except ApiClientError as error:
            print(f"Mailchimp API error: {error.text}")
            return False

    def update_subscriber(self, email: str, merge_fields: Dict[str, Any]) -> bool:
        """
        Update an existing subscriber's information
        """
        try:
            self.client.lists.update_list_member(
                self.audience_id,
                self._get_subscriber_hash(email),
                {"merge_fields": merge_fields}
            )
            return True
        except ApiClientError as error:
            print(f"Mailchimp API error: {error.text}")
            return False

    def _get_subscriber_hash(self, email: str) -> str:
        """
        Get the MD5 hash of the lowercase version of an email
        """
        import hashlib
        return hashlib.md5(email.lower().encode()).hexdigest()