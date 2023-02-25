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

class ActionSetInput_7(Action):
    
    def name(self) -> Text:
  
        return "action_set_input7_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        input7 = tracker.get_slot("input7")
        bot_session_id = tracker.sender_id
        print("bot_session_id", bot_session_id)        
        if input7:
            print("input7_slot",input7) 
            conn = connection()
            result = conn.iwill.bot_emotion.insert_one(
                {
                    "bot_session_id": bot_session_id,
                    "emotion": input7
                }
            )
            # print(result)
            # print(result.inserted_id)
            conn.close()
        dispatcher.utter_message(template="utter_week2_affirm2") 
        return [SlotSet("input7", None)]

class ActionSetInput7(Action):
    
    def name(self) -> Text:
        return "action_set_input7_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input7", None)]

class ActionHelloWorld1(Action):
    
    def name(self) -> Text:
        self.input_all_1 = [ ]
        print("hello")
        return "action_input7_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        bot_session_id = tracker.sender_id
        print("bot_session_id", bot_session_id)

        conn = connection()
        result = conn.iwill.bot_emotion.find(
            {
                "bot_session_id": bot_session_id
            }
        )
        all_emotions1= []
        for doc in result:
            print(doc['emotion']) 
            all_emotions1.append(doc['emotion'])
        print(all_emotions1) 

        last_intent = tracker.latest_message['intent'].get('name')
        print(last_intent) 
 
        input7 = tracker.get_slot("input7")
        if input7:
            print("-------------------------------------")
            print("input7_slot",input7) 
        else:
            print("input7",input7)    
            # dispatcher.utter_message(template="utter_week2_affirm3")
            dispatcher.utter_message(text = "Good job! Here is a list of your favorite activities:- "+'"'+", ".join(all_emotions1)+'"'+".")
            dispatcher.utter_message(text = "Choose one that you would like to start working on this week! Write down the number next to the activity.")
            for i in all_emotions1:
                print(i)
                dispatcher.utter_message(buttons = [{"payload": "/mood_great", "title": str(i)}])     
        return [SlotSet("input7", None)]  
    
class ActionSetInput8(Action):
    
    def name(self) -> Text:
        return "action_set_input8_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input8", None)]    
       

 
class ActionSetInput_10(Action):
    
    def name(self) -> Text:
        global all_input10
        all_input10= []
        self.input10_all = [ ]
        print("input10_saved")
        return "action_set_input10_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        input10_all = [ ]  
        input10 = tracker.get_slot("input10")
        if input10:
            print("input10_slot",input10) 
            input10_all.append(input10) 
            self.input10_all.append(input10)
            all_input10.append(input10)
            print("input10_all",input10_all)
            print("self.input10_all",self.input10_all)
            print("all_input10",all_input10)
        dispatcher.utter_message(template="utter_story_week2_11") 
        return [SlotSet("input10", None)]

class ActionSetInput_11(Action):
    
    def name(self) -> Text:
        global all_input11
        all_input11= []
        self.input11_all = [ ]
        print("input11_saved")
        return "action_set_input11_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        input11_all = [ ]  
        input11 = tracker.get_slot("input11")
        if input11:
            print("input11_slot",input11) 
            input11_all.append(input11) 
            self.input11_all.append(input11)
            all_input11.append(input11)
            print("input11_all",input11_all)
            print("self.input11_all",self.input11_all)
            print("all_input11",all_input11)
        dispatcher.utter_message(template="utter_story_week2_14") 
        return [SlotSet("input11", None)]

 
     
class ActionSetinput10(Action):
    
    def name(self) -> Text:
        return "action_set_input10_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input10", None)] 
 

class ActionSetinput11(Action):
    
    def name(self) -> Text:
        return "action_set_input11_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input11", None)]
    
class ActionSetinput12(Action):
    
    def name(self) -> Text:
        return "action_set_input12_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input12", None)]    

class ActionSetinput13(Action):
    
    def name(self) -> Text:
        return "action_set_input13_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input13", None)]    
    
class ActionSetInput_14(Action):
    
    def name(self) -> Text:
        global all_input14
        all_input14= []
        self.input14_all = [ ]
        print("input14_saved")
        return "action_set_input14_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        input14_all = [ ]  
        input14 = tracker.get_slot("input14")
        if input14:
            print("input14_slot",input14) 
            input14_all.append(input14) 
            self.input14_all.append(input14)
            all_input14.append(input14)
            print("input14_all",input14_all)
            print("self.input14_all",self.input14_all)
            print("all_input14",all_input14)
        dispatcher.utter_message(template="utter_convo2_3") 
        return [SlotSet("input14", None)]

class ActionSetInput_15(Action):
    
    def name(self) -> Text:
        global all_input15
        all_input15= []
        self.input15_all = [ ]
        print("input15_saved")
        return "action_set_input15_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        input15_all = [ ]  
        input15 = tracker.get_slot("input15")
        if input15:
            print("input15_slot",input15) 
            input15_all.append(input15) 
            self.input15_all.append(input15)
            all_input15.append(input15)
            print("input15_all",input15_all)
            print("self.input15_all",self.input15_all)
            print("all_input15",all_input15)
        dispatcher.utter_message(template="utter_affirm11") 
        return [SlotSet("input15", None)]

 
     
class ActionSetinput14(Action):
    
    def name(self) -> Text:
        return "action_set_input14_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input14", None)] 
 

class ActionSetinput15(Action):
    
    def name(self) -> Text:
        return "action_set_input15_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input15", None)]    

     
    
    