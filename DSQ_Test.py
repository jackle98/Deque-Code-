import unittest
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):

    def setUp(self):
        # Run your tests with each deque type to ensure that
        # they behave identically.
        self.__deque = get_deque(LL_DEQUE_TYPE)
        self.__stack = Stack()
        self.__queue = Queue()

    def test_push_on_empty_stack(self):
        self.__stack.push(5)
        self.assertEqual('[ 5 ]', str(self.__stack))

    def test_push_two_values_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.assertEqual('[ 6, 5 ]', str(self.__stack))

    def test_push_three_values_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.__stack.push(7)
        self.assertEqual('[ 7, 6, 5 ]', str(self.__stack))

    def test_push_four_values_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.__stack.push(7)
        self.__stack.push(8)
        self.assertEqual('[ 8, 7, 6, 5 ]', str(self.__stack))

    def test_push_five_values_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.__stack.push(7)
        self.__stack.push(8)
        self.__stack.push(9)
        self.assertEqual('[ 9, 8, 7, 6, 5 ]', str(self.__stack))

    def test_pop_on_empty_stack(self):
        self.__stack.pop()
        self.assertEqual(None, self.__stack.pop())

    def test_pop_on_one_value_stack(self):
        self.__stack.push(5)
        self.assertEqual('5', str(self.__stack.pop()))

    def test_pop_on_two_value_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.assertEqual('6', str(self.__stack.pop()))

    def test_pop_on_three_value_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.__stack.push(7)
        self.assertEqual('7', str(self.__stack.pop()))

    def test_string_pop_on_one_value_stack(self):
        self.__stack.push(5)
        self.__stack.pop()
        self.assertEqual('[ ]', str(self.__stack))

    def test_string_pop_on_two_value_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.__stack.pop()
        self.assertEqual('[ 5 ]', str(self.__stack))

    def test_string_pop_on_three_value_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.__stack.push(7)
        self.__stack.pop()
        self.assertEqual('[ 6, 5 ]', str(self.__stack))

    def test_string_pop_on_four_value_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.__stack.push(7)
        self.__stack.push(8)
        self.__stack.pop()
        self.assertEqual('[ 7, 6, 5 ]', str(self.__stack))

    def test_string_pop_on_five_value_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.__stack.push(7)
        self.__stack.push(8)
        self.__stack.push(9)
        self.__stack.pop()
        self.assertEqual('[ 8, 7, 6, 5 ]', str(self.__stack))

    def test_peek_on_empty_stack(self):
        self.assertEqual(None, self.__stack.peek())

    def test_peek_on_one_value_stack(self):
        self.__stack.push(5)
        self.assertEqual('5', str(self.__stack.peek()))

    def test_peek_on_two_value_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.assertEqual('6', str(self.__stack.peek()))

    def test_peek_on_three_value_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.__stack.push(7)
        self.assertEqual('7', str(self.__stack.peek()))

    def test_peek_on_four_value_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.__stack.push(7)
        self.__stack.push(8)
        self.assertEqual('8', str(self.__stack.peek()))

    def test_peek_on_five_value_stack(self):
        self.__stack.push(5)
        self.__stack.push(6)
        self.__stack.push(7)
        self.__stack.push(8)
        self.__stack.push(9)
        self.assertEqual('9', str(self.__stack.peek()))

    def test_length_on_empty_stack(self):
        self.assertEqual(0, len(self.__stack))

    def test_length_on_one_value_stack_pushing(self):
        self.__stack.push(1)
        self.assertEqual(1, len(self.__stack))

    def test_length_on_two_value_stack_pushing(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.assertEqual(2, len(self.__stack))

    def test_length_on_three_value_stack_pushing(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.assertEqual(3, len(self.__stack))

    def test_length_on_four_value_stack_pushing(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.assertEqual(4, len(self.__stack))

    def test_length_on_five_value_stack_pushing(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.__stack.push(5)
        self.assertEqual(5, len(self.__stack))

    def test_length_on_five_value_stack_popping(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.__stack.push(5)
        self.__stack.pop()
        self.assertEqual(4, len(self.__stack))

    def test_length_on_four_value_stack_popping(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.__stack.pop()
        self.assertEqual(3, len(self.__stack))

    def test_length_on_three_value_stack_popping(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.pop()
        self.assertEqual(2, len(self.__stack))

    def test_length_on_two_value_stack_popping(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.pop()
        self.assertEqual(1, len(self.__stack))

    def test_length_on_one_value_stack_popping(self):
        self.__stack.push(1)
        self.__stack.pop()
        self.assertEqual(0, len(self.__stack))

    def test_enqueue_on_empty_queue(self):
        self.__queue.enqueue(1)
        self.assertEqual('[ 1 ]', str(self.__queue))

    def test_enqueue_on_two_values_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.assertEqual('[ 1, 2 ]', str(self.__queue))

    def test_enqueue_on_three_values_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.assertEqual('[ 1, 2, 3 ]', str(self.__queue))

    def test_enqueue_on_four_values_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.assertEqual('[ 1, 2, 3, 4 ]', str(self.__queue))

    def test_enqueue_on_five_values_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.enqueue(5)
        self.assertEqual('[ 1, 2, 3, 4, 5 ]', str(self.__queue))

    def test_dequeue_on_empty_queue(self):
        self.assertEqual(None, self.__queue.dequeue())

    def test_dequeue_on_one_value_queue(self):
        self.__queue.enqueue(1)
        self.assertEqual('1', str(self.__queue.dequeue()))

    def test_dequeue_on_two_value_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.assertEqual('1', str(self.__queue.dequeue()))

    def test_dequeue_on_three_value_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.assertEqual('1', str(self.__queue.dequeue()))

    def test_string_dequeue_on_one_value_queue(self):
        self.__queue.enqueue(1)
        self.__queue.dequeue()
        self.assertEqual('[ ]', str(self.__queue))

    def test_string_dequeue_on_two_value_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.dequeue()
        self.assertEqual('[ 2 ]', str(self.__queue))

    def test_string_dequeue_on_three_value_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.dequeue()
        self.assertEqual('[ 2, 3 ]', str(self.__queue))

    def test_string_dequeue_on_four_value_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.dequeue()
        self.assertEqual('[ 2, 3, 4 ]', str(self.__queue))

    def test_string_dequeue_on_five_value_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.enqueue(5)
        self.__queue.dequeue()
        self.assertEqual('[ 2, 3, 4, 5 ]', str(self.__queue))

    def test_length_on_empty_queue(self):
        self.assertEqual(0, len(self.__queue))

    def test_length_on_one_value_queue_enqueueing(self):
        self.__queue.enqueue(1)
        self.assertEqual(1, len(self.__queue))

    def test_length_on_two_value_queue_enqueueing(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.assertEqual(2, len(self.__queue))

    def test_length_on_three_value_queue_enqueueing(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.assertEqual(3, len(self.__queue))

    def test_length_on_four_value_queue_enqueueing(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.assertEqual(4, len(self.__queue))

    def test_length_on_five_value_queue_enqueueing(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.enqueue(5)
        self.assertEqual(5, len(self.__queue))

    def test_length_on_five_value_queue_dequeueing(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.enqueue(5)
        self.__queue.dequeue()
        self.assertEqual(4, len(self.__queue))

    def test_length_on_four_value_queue_dequeueing(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.dequeue()
        self.assertEqual(3, len(self.__queue))

    def test_length_on_three_value_queue_dequeueing(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.dequeue()
        self.assertEqual(2, len(self.__queue))

    def test_length_on_two_value_queue_dequeueing(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.dequeue()
        self.assertEqual(1, len(self.__queue))

    def test_length_on_one_value_queue_dequeueing(self):
        self.__queue.enqueue(1)
        self.__queue.dequeue()
        self.assertEqual(0, len(self.__queue))

    def test_pushfront_empty_deque(self):
        self.__deque.push_front(1)
        self.assertEqual('[ 1 ]', str(self.__deque))

    def test_pushfront_two_values_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.assertEqual('[ 2, 1 ]', str(self.__deque))

    def test_pushfront_three_values_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.assertEqual('[ 3, 2, 1 ]', str(self.__deque))

    def test_pushfront_four_values_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.assertEqual('[ 4, 3, 2, 1 ]', str(self.__deque))

    def test_pushfront_five_values_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual('[ 5, 4, 3, 2, 1 ]', str(self.__deque))

    def test_pushback_empty_deque(self):
        self.__deque.push_back(1)
        self.assertEqual('[ 1 ]', str(self.__deque))

    def test_pushback_two_values_deque(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual('[ 1, 2 ]', str(self.__deque))

    def test_pushback_three_values_deque(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))

    def test_pushback_four_values_deque(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.assertEqual('[ 1, 2, 3, 4 ]', str(self.__deque))

    def test_pushback_five_values_deque(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.__deque.push_back(5)
        self.assertEqual('[ 1, 2, 3, 4, 5 ]', str(self.__deque))

    def test_popfront_empty_deque(self):
        self.assertEqual(None, self.__deque.pop_front())

    def test_popfront_one_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.assertEqual(1, self.__deque.pop_front())

    def test_popfront_two_values_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.assertEqual(2, self.__deque.pop_front())

    def test_popfront_three_values_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.assertEqual(3, self.__deque.pop_front())

    def test_popfront_four_values_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.assertEqual(4, self.__deque.pop_front())

    def test_popfront_five_values_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual(5, self.__deque.pop_front())

    def test_popfront_one_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.assertEqual(1, self.__deque.pop_front())

    def test_popfront_two_values_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual(1, self.__deque.pop_front())

    def test_popfront_three_values_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.assertEqual(1, self.__deque.pop_front())

    def test_popfront_four_values_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.assertEqual(1, self.__deque.pop_front())

    def test_popfront_five_values_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.__deque.push_back(5)
        self.assertEqual(1, self.__deque.pop_front())

    def test_popback_on_empty_deque(self):
        self.assertEqual(None, self.__deque.pop_back())

    def test_popback_one_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.assertEqual(1, self.__deque.pop_back())

    def test_popback_two_values_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.assertEqual(1, self.__deque.pop_back())

    def test_popback_three_values_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.assertEqual(1, self.__deque.pop_back())

    def test_popback_four_values_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.assertEqual(1, self.__deque.pop_back())

    def test_popback_five_values_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual(1, self.__deque.pop_back())

    def test_popback_one_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.assertEqual(1, self.__deque.pop_back())

    def test_popback_two_values_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual(2, self.__deque.pop_back())

    def test_popback_three_values_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.assertEqual(3, self.__deque.pop_back())

    def test_popback_four_values_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.assertEqual(4, self.__deque.pop_back())

    def test_popback_five_values_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.__deque.push_back(5)
        self.assertEqual(5, self.__deque.pop_back())

    def test_peekfront_one_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.assertEqual(1, self.__deque.peek_front())

    def test_peekfront_two_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.assertEqual(2, self.__deque.peek_front())

    def test_peekfront_three_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.assertEqual(3, self.__deque.peek_front())

    def test_peekfront_four_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.assertEqual(4, self.__deque.peek_front())

    def test_peekfront_five_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual(5, self.__deque.peek_front())

    def test_peekfront_one_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.assertEqual(1, self.__deque.peek_front())

    def test_peekfront_two_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual(1, self.__deque.peek_front())

    def test_peekfront_three_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.assertEqual(1, self.__deque.peek_front())

    def test_peekfront_four_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.assertEqual(1, self.__deque.peek_front())

    def test_peekfront_five_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.__deque.push_back(5)
        self.assertEqual(1, self.__deque.peek_front())

    def test_peekback_one_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.assertEqual(1, self.__deque.peek_back())

    def test_peekback_two_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.assertEqual(1, self.__deque.peek_back())

    def test_peekback_three_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.assertEqual(1, self.__deque.peek_back())

    def test_peekback_four_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.assertEqual(1, self.__deque.peek_back())

    def test_peekback_five_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual(1, self.__deque.peek_back())

    def test_peekback_one_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.assertEqual(1, self.__deque.peek_back())

    def test_peekback_two_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual(2, self.__deque.peek_back())

    def test_peekback_three_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.assertEqual(3, self.__deque.peek_back())

    def test_peekback_four_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.assertEqual(4, self.__deque.peek_back())

    def test_peekback_five_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.__deque.push_back(5)
        self.assertEqual(5, self.__deque.peek_back())

    def test_string_popfront_on_one_value_deque(self):
        self.__deque.push_front(1)
        self.__deque.pop_front()
        self.assertEqual('[ ]', str(self.__deque))

    def test_string_popfront_on_two_value_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.pop_front()
        self.assertEqual('[ 1 ]', str(self.__deque))

    def test_string_popfront_on_three_value_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.pop_front()
        self.assertEqual('[ 2, 1 ]', str(self.__deque))

    def test_string_popfront_on_four_value_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.pop_front()
        self.assertEqual('[ 3, 2, 1 ]', str(self.__deque))

    def test_string_popfront_on_five_value_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.__deque.pop_front()
        self.assertEqual('[ 4, 3, 2, 1 ]', str(self.__deque))

    def test_string_popback_on_one_value_deque(self):
        self.__deque.push_front(1)
        self.__deque.pop_back()
        self.assertEqual('[ ]', str(self.__deque))

    def test_string_popback_on_two_value_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.pop_back()
        self.assertEqual('[ 2 ]', str(self.__deque))

    def test_string_popback_on_three_value_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.pop_back()
        self.assertEqual('[ 3, 2 ]', str(self.__deque))

    def test_string_popback_on_four_value_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.pop_back()
        self.assertEqual('[ 4, 3, 2 ]', str(self.__deque))

    def test_string_popback_on_five_value_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.__deque.pop_back()
        self.assertEqual('[ 5, 4, 3, 2 ]', str(self.__deque))

    def test_length_on_empty_deque(self):
        self.assertEqual(0, len(self.__deque))

    def test_length_one_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.assertEqual(1, len(self.__deque))

    def test_length_two_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.assertEqual(2, len(self.__deque))

    def test_length_three_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.assertEqual(3, len(self.__deque))

    def test_length_four_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.assertEqual(4, len(self.__deque))

    def test_length_five_value_deque_when_pushingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual(5, len(self.__deque))

    def test_length_one_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.assertEqual(1, len(self.__deque))

    def test_length_two_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual(2, len(self.__deque))

    def test_length_three_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.assertEqual(3, len(self.__deque))

    def test_length_four_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.assertEqual(4, len(self.__deque))

    def test_length_five_value_deque_when_pushingback(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.__deque.push_back(5)
        self.assertEqual(5, len(self.__deque))

    def test_length_one_value_deque_when_poppingfront(self):
        self.__deque.push_front(1)
        self.__deque.pop_front()
        self.assertEqual(0, len(self.__deque))

    def test_length_two_value_deque_when_poppingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.pop_front()
        self.assertEqual(1, len(self.__deque))

    def test_length_three_value_deque_when_poppingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.pop_front()
        self.assertEqual(2, len(self.__deque))

    def test_length_four_value_deque_when_poppingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.pop_front()
        self.assertEqual(3, len(self.__deque))

    def test_length_five_value_deque_when_poppingfront(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.__deque.pop_front()
        self.assertEqual(4, len(self.__deque))

    def test_length_one_value_deque_when_poppingback(self):
        self.__deque.push_front(1)
        self.__deque.pop_back()
        self.assertEqual(0, len(self.__deque))

    def test_length_two_value_deque_when_poppingback(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.pop_back()
        self.assertEqual(1, len(self.__deque))

    def test_length_three_value_deque_when_poppingback(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.pop_back()
        self.assertEqual(2, len(self.__deque))

    def test_length_four_value_deque_when_poppingback(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.pop_back()
        self.assertEqual(3, len(self.__deque))

    def test_length_five_value_deque_when_poppingback(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.__deque.pop_back()
        self.assertEqual(4, len(self.__deque))



if __name__ == '__main__':
    unittest.main()
