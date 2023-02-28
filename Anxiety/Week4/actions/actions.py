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

class ActionSetInput_29(Action):
    
    def name(self) -> Text:
        global all_input
        all_input= []
        self.input29_all = [ ]
        print("input29_saved")
        return "action_set_input29_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        input29_all = [ ]  
        input29 = tracker.get_slot("input29")
        ###########################
        if input29:
            print("input29_slot",input29) 
            input29_all.append(input29) 
            self.input29_all.append(input29)
            all_input.append(input29)
            print("input29_all",input29_all)
            print("self.input29_all",self.input29_all)
            print("all_input",all_input)
        ###########################
        input29 = tracker.get_slot("input29")
        bot_session_id = tracker.sender_id
        print("bot_session_id", bot_session_id)        
        if input29:
            print("input29_slot",input29) 
            conn = connection()
            result = conn.iwill.bot_reason.insert_one(
                {
                    "bot_session_id": bot_session_id,
                    "reason": input29
                }
            )
            print(result)
            print(result.inserted_id)
            conn.close()
        dispatcher.utter_message(template="utter_week4_s86") 
        return [SlotSet("input29", None)]

 
class ActionSetInput12(Action):
    
    def name(self) -> Text:
        return "action_set_input12_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input12", None)]
     
class ActionSetInput13(Action):
    
    def name(self) -> Text:
        return "action_set_input13_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input13", None)] 
 

class ActionSetInput14(Action):
    
    def name(self) -> Text:
        return "action_set_input14_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input14", None)]

class ActionSetInput15(Action):
    
    def name(self) -> Text:
        return "action_set_input15_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input15", None)]  

class ActionSetInput16(Action):
    
    def name(self) -> Text:
        return "action_set_input16_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input16", None)]    
    
class ActionSetInput17(Action):
    
    def name(self) -> Text:
        return "action_set_input17_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input17", None)] 
 

class ActionSetInput18(Action):
    
    def name(self) -> Text:
        return "action_set_input18_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input18", None)]

class ActionSetInput19(Action):
    
    def name(self) -> Text:
        return "action_set_input19_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input19", None)]  

class ActionSetInput20(Action):
    
    def name(self) -> Text:
        return "action_set_input20_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input20", None)]        
    
class ActionSetInput21(Action):
    
    def name(self) -> Text:
        return "action_set_input21_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input21", None)]    
    
class ActionSetInput22(Action):
    
    def name(self) -> Text:
        return "action_set_input22_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input22", None)] 
 
class ActionSetInput22_a(Action):
    
    def name(self) -> Text:
        return "action_set_input22_a_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input22_a", None)]  

class ActionSetInput22_b(Action):
    
    def name(self) -> Text:
        return "action_set_input22_b_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input22_b", None)]  
    
class ActionSetInput22_c(Action):
    
    def name(self) -> Text:
        return "action_set_input22_c_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input22_c", None)] 
        
class ActionSetInput23(Action):
    
    def name(self) -> Text:
        return "action_set_input23_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input23", None)]

class ActionSetInput23_1(Action):
    
    def name(self) -> Text:
        return "action_set_input23_1_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input23_1", None)]  

class ActionSetInput24(Action):
    
    def name(self) -> Text:
        return "action_set_input24_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input24", None)]        

class ActionSetInput24_a(Action):
    
    def name(self) -> Text:
        return "action_set_input24_a_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input24_a", None)]  

class ActionSetInput24_b(Action):
    
    def name(self) -> Text:
        return "action_set_input24_b_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input24_b", None)]  
    
class ActionSetInput24_c(Action):
    
    def name(self) -> Text:
        return "action_set_input24_c_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input24_c", None)] 

    
class ActionSetInput25(Action):
    
    def name(self) -> Text:
        return "action_set_input25_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input25", None)]

class ActionSetInput25_a(Action):
    
    def name(self) -> Text:
        return "action_set_input25_a_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input25_a", None)]  

class ActionSetInput25_b(Action):
    
    def name(self) -> Text:
        return "action_set_input25_b_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input25_b", None)]  
    
class ActionSetInput25_c(Action):
    
    def name(self) -> Text:
        return "action_set_input25_c_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input25_c", None)] 

     
class ActionSetInput26(Action):
    
    def name(self) -> Text:
        return "action_set_input26_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input26", None)] 
 

class ActionSetInput27(Action):
    
    def name(self) -> Text:
        return "action_set_input27_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input27", None)]

class ActionSetInput28(Action):
    
    def name(self) -> Text:
        return "action_set_input28_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input28", None)]  

class ActionSetInput28_a(Action):
    
    def name(self) -> Text:
        return "action_set_input28_a_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input28_a", None)] 

class ActionSetInput29(Action):
    
    def name(self) -> Text:
        return "action_set_input29_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input29", None)] 

class ActionSetInput30(Action):
    
    def name(self) -> Text:
        return "action_set_input30_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input30", None)]    
    
class ActionSetInput32(Action):
    
    def name(self) -> Text:
        return "action_set_input32_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input32", None)] 
 
class ActionSetInput33(Action):
    
    def name(self) -> Text:
        return "action_set_input33_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input33", None)]

class ActionSetInput34(Action):
    
    def name(self) -> Text:
        return "action_set_input34_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input34", None)]  

class ActionSetInput35(Action):
    
    def name(self) -> Text:
        return "action_set_input35_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input35", None)]        
    
class ActionSetInput36(Action):
    
    def name(self) -> Text:
        return "action_set_input36_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input36", None)]    
    
class ActionSetInput37(Action):
    
    def name(self) -> Text:
        return "action_set_input37_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input37", None)] 
 

class ActionSetInput38(Action):
    
    def name(self) -> Text:
        return "action_set_input38_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input38", None)]
    
class ActionSetInput39(Action):
    
    def name(self) -> Text:
        return "action_set_input39_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input39", None)]    
    
class ActionSetInput40(Action):
    
    def name(self) -> Text:
        return "action_set_input40_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input40", None)] 
 

class ActionSetInput41(Action):
    
    def name(self) -> Text:
        return "action_set_input41_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input41", None)]    
    
class ActionHelloWorld29(Action):
    
    def name(self) -> Text:
        self.input_all_1 = [ ]
        print("hello")
        return "action_input29_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ###########################
        bot_session_id = tracker.sender_id
        print("bot_session_id", bot_session_id)
        conn = connection()
        result = conn.iwill.bot_reason.find(
            {
                "bot_session_id": bot_session_id
            }
        )
        all_reasons= []
        for doc in result:
            print(doc['emotion']) 
            all_reasons.append(doc['emotion'])
        print(all_reasons)
        ###########################
        input_all = [ ]    
        last_intent = tracker.latest_message['intent'].get('name')
        print(last_intent)      

        input29 = tracker.get_slot("input29")
        all_reasons_len = len(all_reasons)
        if int(all_reasons_len) <= 3 :
 
            dispatcher.utter_message(text = "Please think of a few more things to add. You can add them even if the chance is very low! ")
            dispatcher.utter_message(buttons = [{"payload": "/affirm8", "title": "Yes."}])
 
        else:
            print("input29",input29)    
            # dispatcher.utter_message(template="utter_week4_s86_b")
            dispatcher.utter_message(text = "Here is what you typed:- "+'"'+", ".join(all_reasons)+'"'+".") 
            dispatcher.utter_message(buttons = [{"payload": "/affirm9", "title": "Yes."}])
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return [SlotSet("input29", None)]     
    
    
class ActionHelloWorld29_1(Action):
    
    def name(self) -> Text:
        self.input_all_1 = [ ]
        print("hello")
        return "action_input29_1_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ###########################
        bot_session_id = tracker.sender_id
        print("bot_session_id", bot_session_id)
        conn = connection()
        result = conn.iwill.bot_reason.find(
            {
                "bot_session_id": bot_session_id
            }
        )
        all_reasons= []
        for doc in result:
            print(doc['emotion']) 
            all_reasons.append(doc['emotion'])
        print(all_reasons)
        ###########################

        input29 = tracker.get_slot("input29")
        last_input = all_input[-1]
        rev_input = all_reasons.reverse()
        print("rev_input",rev_input)
        # if last_input :
        #     print("-------------------------------------")
        #     dispatcher.utter_message(text = "1." +str(last_input))
        if rev_input :
            for i in rev_input:
                print("-------------------------------------")
                dispatcher.utter_message(text = "1." +str(i))

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return [SlotSet("input29", None)]  