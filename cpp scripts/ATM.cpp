#include<iostream>
#include<conio.h>
#include<string>

using namespace std;

// Mini Project of ATM Machine

class ATM
{
private:
    long int account_no;
    string name;
    int PIN;
    double balance;
    string mob_no;

public:
    // setData function is setting the Data into the private member variables
    void setData(long int account_No_a, string name_a, int PIN_a, double balance_a, string mobile_No_a)
    {
        account_no = account_No_a;
        name = name_a;
        PIN = PIN_a;
        balance = balance_a;
        mob_no = mobile_No_a;
    }

    long int getAccountNo() { return account_no; }

    string getName() { return name; }

    int getPIN() { return PIN; }

    double getBalance() { return balance; }

    string getMobileNo() { return mob_no; }

    // setMobile function is Updating the user mobile no
    void setMobile(string mob_prev, string mob_new)
    {
        if (mob_prev == mob_no)
        {
            mob_no = mob_new;
            cout << endl << "Sucessfully Updated Mobile no.";
            _getch(); // getch is to hold the screen ( untill user press any key )	from conio.h library
        }

        else
        {
            cout << endl << "Incorrect Old Mobile no. !";
            _getch();
        }
    }
    // cashWithDraw function is used to withdraw money from ATM
    void cashWithdraw(int amount_a)
    {
        if (amount_a > 0 && amount_a < balance)
        {
            balance -= amount_a;
            cout << endl << "Please Collect Your Cash $$";
            cout << endl << "Available Balance : " << balance;
            _getch();
        }

        else
        {
            cout << endl << "Invalid Input or Insufficient Balance :(";
            _getch();
        }
    }
};

int main()
{
    int choice = 0, enterPIN; // enterPIN and enterAccountNo. ---> user authentication
    long int enterAccountNo;

    system("cls");

    // created User ( object )
    ATM user1;
    // Set User Details ( into object )         ( Setting Default Data )
    user1.setData(1234567, "Mike", 1234, 4500.50, "9087654321");

    do
    {
        system("cls");

        cout << endl << "****Welcome to ATM*****" << endl;
        cout << endl << "Enter Your Account No "; // asking user to enter account no
        cin >> enterAccountNo;

        cout << endl << "Enter PIN "; // asking user to enter PIN
        cin >> enterPIN;

        // check whether enter values matches with user details
        if ((enterAccountNo == user1.getAccountNo()) && (enterPIN == user1.getPIN()))
        {
            do
            {
                int amount = 0;
                string oldMobileNo, newMobileNo;

                system("cls");
                // user Interface
                cout << endl << "**** Welcome to ATM *****" << endl;
                cout << endl << "Select Options ";
                cout << endl << "1. Check Balance";
                cout << endl << "2. Cash withdraw";
                cout << endl << "3. Show User Details";
                cout << endl << "4. Update Mobile no.";
                cout << endl << "5. Exit" << endl;
                cin >> choice; // taking user choice

                switch (choice) // switch condition
                {
                case 1:
                    cout << endl << "Your Bank balance is :" << user1.getBalance();
                    _getch();
                    break;

                case 2:
                    cout << endl << "Enter the amount :";
                    cin >> amount;
                    user1.cashWithdraw(amount); // calling cashWithdraw function
                    break;

                case 3:
                    cout << endl << "*** User Details are :- ";
                    cout << endl << "-> Account no" << user1.getAccountNo();
                    cout << endl << "-> Name      " << user1.getName();
                    cout << endl << "-> Balance   " << user1.getBalance();
                    cout << endl << "-> Mobile No." << user1.getMobileNo();
                    _getch();
                    break;

                case 4:
                    cout << endl << "Enter Old Mobile No. ";
                    cin >> oldMobileNo;

                    cout << endl << "Enter New Mobile No. ";
                    cin >> newMobileNo;

                    user1.setMobile(oldMobileNo, newMobileNo);
                    break;

                case 5:
                    exit(0); // exit application

                default: // handle invalid user inputs
                    cout << endl << "Enter Valid Data !!!";
                }

            } while (1); // MENU	   // condition will always TRUE and loop is capable of running infinite times
        }
        else
        {
            cout << endl << "User Details are Invalid !!! ";
            _getch();
        }
    } while (1); // LOGIN		// condition will always TRUE and loop is capable of running infinite times

    return 0;
}
