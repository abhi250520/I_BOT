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

class ActionSetInput7(Action):

    def name(self) -> Text:
        return "action_set_input7_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input7", None)]
 
class ActionSetName(Action):
    
    def name(self) -> Text:
        return "action_set_name_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("name", None)]     

class ActionSetInput_3(Action):
    
    def name(self) -> Text:
        global all_input
        all_input= []
        self.input3_all = [ ]
        print("input3_saved")
        return "action_set_input3_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        input3_all = [ ]  
        input3 = tracker.get_slot("input3")
        if input3:
            print("input3_slot",input3) 
            input3_all.append(input3) 
            self.input3_all.append(input3)
            all_input.append(input3)
            print("input3_all",input3_all)
            print("self.input3_all",self.input3_all)
            print("all_input",all_input)
        dispatcher.utter_message(template="utter_guided_trymore") 
        return [SlotSet("input3", None)]


class ActionSetInput0(Action):
    
    def name(self) -> Text:
        return "action_set_input0_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input0", None)]

class ActionSetInput1(Action):

    def name(self) -> Text:
        return "action_set_input1_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input1", None)]

class ActionSetInput2(Action):
    
    def name(self) -> Text:
        return "action_set_input2_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input2", None)]
     
class ActionSetInput3(Action):
    
    def name(self) -> Text:
        return "action_set_input3_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input3", None)] 
 

class ActionSetInput4(Action):
    
    def name(self) -> Text:
        return "action_set_input4_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input4", None)]

class ActionSetInput5(Action):
    
    def name(self) -> Text:
        return "action_set_input5_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input5", None)]  

class ActionSetInput6(Action):
    
    def name(self) -> Text:
        return "action_set_input6_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input6", None)]

class ActionSetInput8(Action):
    
    def name(self) -> Text:
        return "action_set_input8_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input8", None)]
    
class ActionSetInput9(Action):
    
    def name(self) -> Text:
        return "action_set_input9_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input9", None)]    
    
class ActionSetInput10(Action):
    
    def name(self) -> Text:
        return "action_set_input10_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input10", None)]        

class ActionSetInput11(Action):
    
    def name(self) -> Text:
        return "action_set_input11_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   
        return [SlotSet("input11", None)]   

class ActionHelloWorld(Action):
    
    def name(self) -> Text:
        self.input_all = [ ]
        print("hello")
        return "action_input0_1_2_3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        input_all = [ ]    
        last_intent = tracker.latest_message['intent'].get('name')
        print(last_intent)
        input0 = tracker.get_slot("input0")
        if input0:
            print("input0_slot",input0)
        #     dispatcher.utter_message(template="utter_input3_0")

        input2 = tracker.get_slot("input2")
        if input2:
            print("input2_slot",input2)

        input3 = tracker.get_slot("input3")
        if input3:
            print("-------------------------------------")
            print("input3_slot",input3) 
            input_all.append(input3) 
            self.input_all.append(input3)
            print("input_all",input_all)
            print("self.input_all",self.input_all)
            print("-------------------------------------")

        input1 = tracker.get_slot("input1")
        if input1:
            print("input1",input1)
            # dispatcher.utter_message(template="utter_input3_1")
            dispatcher.utter_message(text = "When you face situations like "+'"'+str(input0)+", "+str(input1)+'"'+", you think that "+'"'+str(input2)+'"'+". This makes you feel "+'"'+", ".join(all_input)+'"'+". Am I right?")
            dispatcher.utter_message(buttons = [{"payload": "/okay_story_part_4", "title": "Exactly..."}])
        else:
            # dispatcher.utter_message(template="utter_input3_0")
            dispatcher.utter_message(text = "When you face situations like "+'"'+str(input0)+'"'+", you think that "+'"'+str(input2)+'"'+". This makes you feel "+'"'+", ".join(all_input)+'"'+". Am I right?")
            dispatcher.utter_message(buttons = [{"payload": "/okay_story_part_4", "title": "Exactly..."}])
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return [SlotSet("input3", None)] 
 
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