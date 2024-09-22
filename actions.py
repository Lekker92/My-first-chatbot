from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBookTicket(Action):
    def name(self) -> Text:
        return "action_book_ticket"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        destination = tracker.get_slot('destination')
        if destination:
            dispatcher.utter_message(text=f"Booking a ticket to {destination} for you.")
        else:
            dispatcher.utter_message(text="Please provide a destination.")
        return []

class ActionAskMenu(Action):
    def name(self) -> Text:
        return "action_ask_menu"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Here are some recommendations from the menu: ...")
        return []

class ActionTroubleshoot(Action):
    def name(self) -> Text:
        return "action_troubleshoot"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product = tracker.get_slot('product')
        if product:
            dispatcher.utter_message(text=f"Let me help you troubleshoot your {product}. What seems to be the issue?")
        else:
            dispatcher.utter_message(text="Please specify the product you need help with.")
        return []
