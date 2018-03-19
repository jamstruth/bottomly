# coding=utf-8
from commands import WikipediaSearchCommand
from slack_channel.abstract_event_handler import AbstractEventHandler


command_symbol = "wik"

class WikipediaEventHandler(AbstractEventHandler):
    def can_handle(self, slack_event):
        text = slack_event["text"]
        return text.startswith(self.command_trigger)

    def handle(self, slack_event):
        q = slack_event["text"][len(self.command_trigger):]
        c = WikipediaSearchCommand()
        result = c.execute(q)
        if result is None:
            response_message = "No results found for \"" + q +  "\""
        else:
            response_message = result["text"] + " " + result["link"]
        if self.debug:
            response_message = "[DEBUG] " + response_message
        self._send_response(response_message, slack_event)

    def _get_command_symbol(self):
        return command_symbol