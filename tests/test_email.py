import pytest
import smtplib
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager
from unittest.mock import patch

    
@pytest.mark.asyncio
@patch("app.services.email_service.EmailService.send_user_email", return_value=None)
async def test_send_markdown_email(mock_send, email_service):
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123"
    }
    await email_service.send_user_email(user_data, 'email_verification')
    mock_send.assert_called_once()
