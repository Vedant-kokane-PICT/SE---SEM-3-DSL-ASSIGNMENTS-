//============================================================================
// Name        : 21415_Assignment_8.cpp
// Author      : Vedant Kokane
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

// 21415 - Vedant Kokane
// Batch - E4


#include <iostream>
#include <string.h>
using namespace std;
class node{
	public :
	int start;
	int end;
	int min;
	int max;
	bool flag;
	string status;
	node *next_node;

	public :
	// default Constructor
	node(){
		start = 0;
		end = 0;
		min = 0;
		max = 0;
		flag = 0;
		next_node = NULL;
	}


};

class linked_list{
	node *head,*last;
	int total_slots;
public :
	linked_list(){
		head = NULL;
		last = NULL;

		total_slots = 0;
	}
	void create_shedule(){
		//int total_slots;
		cout<<"Please enter the total number of slots"<<endl;
		cin>>total_slots;
		// Here we allocated dynamic memory
		for(int i=0;i<total_slots;i++){
			node *temp = new node();
			// Here we read the data
			cout<<"Slot "<<i+1<<endl;
			cout<<"Enter Starting time"<<endl;
			cin>>temp->start;
			cout<<"Enter ending time"<<endl;
			cin>>temp->end;
			cout<<"Enter minimum time"<<endl;
			cin>>temp->min;
			temp->max = temp->end - temp->start;
			temp->flag = 0;
			temp->status = "Available";
			temp->next_node = NULL;
			if(head==NULL){
			head = temp;
			last = head;
			}
			else{
			last->next_node = temp;
			last = last->next_node;
			}
		}
	}

	// function for displaying Appointment Schedule
	void display_schedule(){
		int count = 0;
		cout<<"The Appointment Schedule is "<<endl;
		cout<<"sr no  Start_time  End_time  Minimum_hours  Maximum_hours  Status"<<endl;
		node *temp = new node();
		temp = head;
		while(temp != NULL){
			cout<<count+1;
			cout<<"       "<<temp->start;
			cout<<"          "<<temp->end;
			cout<<"                 "<<temp->min;
			cout<<"              "<<temp->max;
			cout<<"      "<<temp->status;
			cout<<endl;
			temp = temp->next_node;
			count++;
		}
	}

	// Function for Booking appointment
	void book_appointment(){
		int start;
		cout<<"Please enter Appointment time"<<endl;
		cin>>start;
		node *temp = new node();
		temp = head;
		while(temp != NULL){
			if(start == temp->start){
				if(temp->flag == 0){
					cout<<"Appointment is booked"<<endl;
					temp->flag = 1;
					temp->status = "Booked";
				}
				else{
					cout<<"Appointment is not available"<<endl;
				}
			}
			temp = temp->next_node;
		}
	}

	// Function to cancel Appointment
	void cancel_appointment(){
		int start;
		cout<<"Please enter Appointment time to cancel the appointment"<<endl;
		cin>>start;
		node *temp = new node();
		temp = head;
		while(temp != NULL){
			if(start == temp->start){
				if(temp->flag == 1){
					cout<<"Appointment is Cancelled"<<endl;
					temp->flag = 0;
					temp->status ="Available";
				}
				else{
					cout<<"Appointment was not booked"<<endl;
				}
			}
			temp = temp->next_node;
		}
	}

	// for sorting the applications (values swapping)
	void sorting_applications(){
		node *temp = new node();
		int value;
		for(int i = 0;i<total_slots-1;i++){
			temp = head;
			while(temp->next_node != NULL){
				if((temp->start) > (temp->next_node->start)){
					// swapping the start time
					value = temp->start;
					temp->start = temp->next_node->start;
					temp->next_node->start = value;

					// swapping the end time
					value = temp->end;
					temp->end = temp->next_node->end;
					temp->next_node->end = value;

					// swapping the minimum time
					value = temp->min;
					temp->min = temp->next_node->min;
					temp->next_node->min = value;

					// swapping the maximum time
					value = temp->max;
					temp->max = temp->next_node->max;
					temp->next_node->max = value;
				}
				temp = temp->next_node;
			}
		}
	}

	node* swap(node* ptr1, node* ptr2){
		node* tmp = ptr2->next_node;
		ptr2->next_node = ptr1;
		ptr1->next_node = tmp;
		return ptr2;
	}

	// for sorting the applications using pointer manipulation
	void sort_by_pointers(){
		bubbleSort(&head,total_slots);
	}

	// for sorting using bubblesort which uses pointer manipulation
	void bubbleSort(node** head, int total)
{
    node** h;
    int i, j, swapped;
    for (i = 0; i <= total; i++)
    {
        h = head;
        swapped = 0;
        for (j = 0; j < total - i - 1; j++)
        {
            node* p1 = *h;
            node* p2 = p1->next_node;
            if (p1->start > p2->start)
            {
                // update the link after swapping 
                *h = swap(p1, p2);
                swapped = 1;
            }
            h = &(*h)->next_node;
        }
        // break if the loop ended without any swap 
        if (swapped == 0)
            break;
    }
}



};

int main() {
	char a='y';
	linked_list x;
	x.create_shedule();
	x.sort_by_pointers();
	x.display_schedule();
	while(a != 'n'){
		int choice;
		cout<<"1. Book an appointment "<<endl;
		cout<<"2. Cancel an appointment"<<endl;
		cout<<"3. Display Appointment Schedule"<<endl;
		cin>>choice;
		if(choice == 1){
			x.book_appointment();
		}
		else if(choice == 2){
			x.cancel_appointment();
		}
		else if(choice==3){
			x.display_schedule();
		}

		cout<<"Do you want to perform any operation again (y/n)"<<endl;
		cin>>a;
	}
	return 0;
}
