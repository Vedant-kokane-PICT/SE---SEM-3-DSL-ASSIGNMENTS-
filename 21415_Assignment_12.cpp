//============================================================================
// Name        : 21415_Assignment_12.cpp
// Author      : Vedant Kokane
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

// 21415 - Vedant Kokane

#include <iostream>
#include <string.h>
using namespace std;

#define m 10

template <class T>
class item{
	private:
	T id;
	int priority;
	public:
	friend class priority_queue;
	void input(){
        cin>>id>>priority;
    }
	bool operator <= (item x){
		if(x.priority <= priority){
			return 0;
		}
		else{
			return 1;
		}
	}
};


class priority_queue{
	private:
	item<string> p_queue_array[m];
	int front;
	int rear;
	public:
	priority_queue(){
		front = -1;
		rear = -1;
	}

	void enqueue(item<string> i1){
		if(is_full()){
			cout<<"Full"<<endl;
			return;
		}
		else if(is_empty()){
			front = 0;
			rear = 0;
			p_queue_array[rear].id = i1.id;
			p_queue_array[rear].priority = i1.priority;
		}
		else{
			rear++;
			int j = rear-1;
			while(p_queue_array[j] <= i1 && j>=0){
				p_queue_array[j+1] = p_queue_array[j];
				j--;
			}
			p_queue_array[j+1].id = i1.id;
			p_queue_array[j+1].priority = i1.priority;
		}
	}

	void display(){
		int i = front;
		cout<<p_queue_array[i].id<<" "<<p_queue_array[i].priority<<endl;

	}

	void dequeue(){
		if(front == -1 || front == rear+1){
			return;
		}
		else{
			front++;
		}
	}

	bool is_empty(){
		if(front == -1 || front == rear +1){
			return 1;
		}
		return 0;
	}

	bool is_full(){
		if(rear == m-1){
			return 1;
		}
		return 0;
	}
};


int main(){
	string x;
	int y;
	class priority_queue p1;
    item<string> i1;
	char c = 'y';
    while(c != 'n'){
        cout<<"1. Enqueue"<<endl;
        cout<<"2. Dequeue"<<endl;
        cout<<"3. Display "<<endl;
        int choice;
		cin>>choice;
		switch (choice)
        {
        case 1:
            cout<<"Enter an element and its priority"<<endl;
            i1.input();
            p1.enqueue(i1);
            break;
        case 2:
            p1.dequeue();
            break;
		case 3:
			p1.display();
			break;
		}
		cout<<"Do you want to try any other operation (y/n)"<<endl;
        cin>>c;
    }
	return 0;
}
