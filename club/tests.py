from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import MeetingForm

# Create your tests here.
class MeetingTest(TestCase):
    def setup(self):
        meeting=Meeting(meetingtitle='Online Python Training', meetingdate='2021-04-02', location='online', agenda='Learning Python During The Pandemic')
        return meeting
    def test_typestring(self):
        prod = self.setup()
        self.assertEqual(str(prod), prod.meetingtitle)  

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setup(self):
        self.meetingid=Meeting(meetingtitle='Weekend meeting')
        self.attendance=User(username='hien')
        self.meetingminutes=MeetingMinutes(attendance=self.userid, minutestext='30 minutes', meetingid=self.meetingid)
        

    def test_typestring(self):
        text = self.setup()
        self.assertEqual(str(text), text.minutestext)

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def setup(self):
        
        self.resource=Resource(resourcename='Python Crash Course', resourcetype='book', url='https://www.python.org/', dateentered='2021-04-02', description='This book is well written and nicely organized.')
        
    def test_typestring(self):
       name=Resource(resourcename='Python Crash Course')
       self.assertEqual(str(name), name.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setup(self):
        self.userid=User(username='hien')
        self.event=Event(title='Python for Beginner', location='Seattle', date='2021-04-02', description='A great event for Python beginner.', userid=self.userid)
        

    def test_typestring(self):
        prod = self.setup()
        self.assertEqual(str(prod), prod.title)  

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class NewMeetingForm(TestCase):
    
    def test_meetingform(self):
        data={
                'meetingtitle':'Weekend meeting', 
                'meetingdate':'2021-01-16', 
                'meetingtime':'12:00:00', 
                'location':'Tacoma', 
                'agenda':'Python for web design'
            }
        form=MeetingForm (data) 
        self.assertTrue(form.is_valid)
    #this test is failing
    def test_meetingform_Invalid(self):
        data={
                'meetingtitle':'Weekend meeting', 
                'meetingdate':'January 2, 2020',  
                'location':'Tacoma', 
                'agenda':'Python for web design'
            }
        form=MeetingForm (data) 
        self.assertFalse(form.is_valid)

class NewResourceForm(TestCase):
    
    def test_resourceform(self):
        data={
                'resourcename':'python website',
                'resourcetype':'book',
                'url':'https://www.python.org/',
                'dateentered':'2021-01-27',
                'userid':'hao',
                'description':'a good resource for beginer'
            }
        form=ResourceForm (data) 
        self.assertTrue(form.is_valid)
    #this test is failing
    def test_resourceform_Invalid(self):
        data={
                'resourcename':'python website',
                'resourcetype':'book',
                'url':'https://www.python.org/',
                'dateentered':'January 2, 2020',
                'userid':'hao',
                'description':'a good resource for beginer'
            }
        form=ResourceForm (data) 
        self.assertFalse(form.is_valid)


