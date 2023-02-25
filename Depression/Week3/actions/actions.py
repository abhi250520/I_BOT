# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import logging
import json
from datetime import datetime
from typing import Any, Dict, List, Text, Optional
import pymongo

from rasa_sdk import Action, Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormValidationAction, FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
)
 

USER_INTENT_OUT_OF_SCOPE = "out_of_scope"

logger = logging.getLogger(__name__)

"""_summary_
    Update the Slot Value of Input7 to None
Returns:
    Slot to None
"""
 
"""_summary_
    Update the Slot Value of Input3 to None
Returns:
    Slot to None
"""

def connection():
    try:
        conn_str = 'mongodb+srv://dev_admin:mpB1zujXTI1DdJxS@psybot1.14npa.mongodb.net/prod_psybot1?authSource=admin&retryWrites=true&w=majority'
        db = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
        # collection = db.iwill.bot_emotion
        # print("...........",db.server_info())
        print("connected...........")
    except Exception:
        print("Unable to connect to the server................")
    return db

class ActionSaveName(Action):
    
    def name(self) -> Text:
        return "action_save_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        bot_session_id = tracker.sender_id
        print("bot_session_id", bot_session_id)
        if name:
            print("name_slot",name) 
            conn = connection()
            result = conn.iwill.bot_username.insert_one(
                {
                    "bot_session_id": bot_session_id,
                    "username": name
                }
            )
            print(result)
            print(result.inserted_id)
            result = conn.iwill.bot_username.find(
            {
                "bot_session_id": bot_session_id
            }
            )
            names = []
            for doc in result:
                print(doc['username']) 
                names.append(doc['username'])
            print(names)
            conn.close()
        #dispatcher.utter_message(template="utter_guided_trymore") 
        return [SlotSet("name", name)] 

class ActionGetName(Action):
    
    def name(self) -> Text:
        return "action_get_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        bot_session_id = tracker.sender_id
        print("bot_session_id", bot_session_id)
        print("name_slot",name) 
        conn = connection()
        result = conn.iwill.bot_username.find(
            {
                "bot_session_id": bot_session_id
            }
        )
        names = []
        for doc in result:
            print(doc['username']) 
            names.append(doc['username'])
        print(names)
        name = names[0]
        return [SlotSet("name", name)]


class ActionSetName(Action):
    
    def name(self) -> Text:
        return "action_set_name_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("name", None)] 
    
class ActionSetinput16(Action):
    
    def name(self) -> Text:
        return "action_set_input16_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input16", None)] 
 

class ActionSetinput17(Action):
    
    def name(self) -> Text:
        return "action_set_input17_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input17", None)]       

class ActionSetinput18(Action):
    
    def name(self) -> Text:
        return "action_set_input18_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input18", None)] 
 

class ActionSetinput19(Action):
    
    def name(self) -> Text:
        return "action_set_input19_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input19", None)]   

class ActionSetinput9(Action):
    
    def name(self) -> Text:
        return "action_set_input9_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input9", None)]     
    
    