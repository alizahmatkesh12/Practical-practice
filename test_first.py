from unittest import TestCase
import trace_back
import traceback

# class FirstTests(TestCase):
#     def test_many(self):
#         self.assertEqual(trace_back.first([x for x in range(5)]), 0)
        
#     def test_one(self):
#         self.assertEqual(trace_back.first([3]), 3)
        
#     def test_empty(self):
#         self.assertEqual(trace_back.first([], "a"), "a")
        
#     def test_empty_stop_Iteration(self):
#         try:
#             trace_back.first([])                       
#         except ValueError:
#             format_exec = traceback.format_exc()
#             self.assertIn("StopIteration", format_exec) 
#             self.assertIn("The above exception was the direct cause", format_exec)
            
#         else:
#             self.fail()              

class FirstTests(TestCase):
    def test_many(self):
        self.assertEqual(trace_back.first([x for x in range(10)]), 0) 

    
    def test_one(self):
        self.assertEqual(trace_back.first([3]), 3)
        
        
        
    def test_empty(self):
        self.assertEqual(trace_back.first([], "a"), "a")
    def test_empty_stop_Iteration(self):
        try:
            trace_back.first([])
        except ValueError:
            format_exec = traceback.format_exc()
            self.assertIn("StopIteration", format_exec)
            self.assertIn("The above exception was the direct cause", format_exec)                   

        else:
            self.fail()
