#ifndef JoelJebitto_H
#define JoelJebitto_H
#include <iostream>

using namespace std;

class Book
{
public:
    string title;
    string auther;

    int pages;
};

class Car
{
public:
    string AcarName;
    int AnumberOfWheel;
    int ArateOfCar;

    Car(string carName, int numberOfWheel, int rateOfCar)
    {
        AcarName = carName;
        AnumberOfWheel = numberOfWheel;
        ArateOfCar = rateOfCar;
    }

    void info()
    {
        cout << "name of car : " << AcarName << endl;
        cout << "number of wheel : " << AnumberOfWheel << endl;
        cout << "rate of car : " << ArateOfCar << endl;
    }
};

class Bus
{
public:
    string AbusName;
    int AnumberOfWheel;
    int ArateOfBus;

    Bus(string busName, int numberOfWheel, int rateOfBus)
    {
        AbusName = busName;
        AnumberOfWheel = numberOfWheel;
        ArateOfBus = rateOfBus;
    }

    void info()
    {
        cout << "name of Bus : " << AbusName << endl;
        cout << "number of wheel : " << AnumberOfWheel << endl;
        cout << "rate of bus : " << ArateOfBus << endl;
    }
};

template <typename INCOME, typename MARK>
class Student
{

public:
    string name;
    int age;
    MARK mark;
    INCOME familyIncome;

    Student(string nameS, int ageS, MARK markS, INCOME familyIncomeS)
    {
        name = nameS;
        age = ageS;
        mark = markS;
        familyIncome = familyIncomeS;
    }

    void showinfo()
    {
        cout << "Name : " << name << endl;
        cout << "Age : " << age << endl;
        cout << "Mark : " << mark << endl;
        cout << "Family Income : " << familyIncome << endl;
    }
};

class Calculator
{
public:
    Calculator()
    {
        int num1, num2, index = 0, result;
        char op;
        bool run = true;
        while (run)
        {

            cout << "Enter first number : ";
            cin >> num1;

            cout << "Enter operator : ";
            cin >> op;

            cout << "Enter secend number : ";
            cin >> num2;

            switch (op)
            {
            case '+':
                result = num1 + num2;
                break;

            case '-':
                result = num1 - num2;
                break;

            case '*':
                result = num1 * num2;
                break;

            case '/':
                result = num1 / num2;
                break;

            case '%':
                result = num1 % num2;
                break;

            default:
                cout << "can not find operator" << endl;
                break;
            }

            cout << "Answer is " << result << endl;

            result = 0;

            index++;
        }
    }
};

class NoteBook
{
private:
    string TitleN;
    int NumberOfPagesN;

public:
    NoteBook(string Title, int NumberOfPages)
    {
        TitleN = Title;
        NumberOfPagesN = NumberOfPages;
    }
    void info()
    {
        cout << "Title : " << TitleN << endl;
        cout << "Number of pages : " << NumberOfPagesN << endl;
    }
};

template <typename B, typename L>
class House
{
private:
    B breathOfTheRoom;
    L lengthOfTheRoom;
    int numberOfFans,
        numberOfRooms,
        numberOfTabels,
        numberOfChair,
        numberOfComputer,
        numberOfPhone,
        numberOfFamilyMembers,
        numberOfAc,
        numberOfTubeLight,
        numberOfBooks,
        numberOfWindos,
        numberOfDoors;

    void SetNumberOfFans(int value)
    {
        numberOfFans = value;
    }

    void SetNumberOfRooms(int value)
    {
        numberOfRooms = value;
    }

    void SetBreathOfTheRoom(int value)
    {
        breathOfTheRoom = value;
    }

    void SetLengthOfTheRoom(int value)
    {
        lengthOfTheRoom = value;
    }
    void SetNumberOfTabels(int value)
    {
        numberOfTabels = value;
    }

    void SetNumberOfChair(int value)
    {
        numberOfChair = value;
    }

    void SetNumberOfComputer(int value)
    {
        numberOfComputer = value;
    }

    void SetNumberOfPhone(int value)
    {
        numberOfPhone = value;
    }

    void SetNumberOfFamilyMembers(int value)
    {
        numberOfFamilyMembers = value;
    }

    void SetNumberOfAc(int value)
    {
        numberOfAc = value;
    }

    void SetNumberOfTubeLight(int value)
    {
        numberOfTubeLight = value;
    }

    void SetNumberOfBooks(int value)
    {
        numberOfBooks = value;
    }

    void SetNumberOfWindos(int value)
    {
        numberOfWindos = value;
    }

    void SetNumberOfDoors(int value)
    {
        numberOfDoors = value;
    }

public:
    House(int NumberOfRooms,
          B BreathOfTheRoom,
          L LengthOfTheRoom,
          int NumberOfFans,
          int NumberOfTabels,
          int NumberOfChair,
          int NumberOfComputer,
          int NumberOfPhone,
          int NumberOfFamilyMembers,
          int NumberOfAc,
          int NumberOfTubeLight,
          int NumberOfBooks,
          int NumberOfWindos,
          int NumberOfDoors)
    {
        SetNumberOfFans(NumberOfFans);
        SetNumberOfRooms(NumberOfRooms);
        SetBreathOfTheRoom(BreathOfTheRoom);
        SetLengthOfTheRoom(LengthOfTheRoom);
        SetNumberOfTabels(NumberOfTabels);
        SetNumberOfChair(NumberOfChair);
        SetNumberOfComputer(NumberOfComputer);
        SetNumberOfPhone(NumberOfPhone);
        SetNumberOfFamilyMembers(NumberOfFamilyMembers);
        SetNumberOfAc(NumberOfAc);
        SetNumberOfBooks(NumberOfBooks);
        SetNumberOfWindos(NumberOfWindos);
        SetNumberOfDoors(NumberOfDoors);
    }

    // get

    int GetNumberOfFans()
    {
        return numberOfFans;
    }

    int GetNumberOfRooms()
    {
        return numberOfRooms;
    }

    B GetBreathOfTheRoom()
    {
        return breathOfTheRoom;
    }

    L GetLengthOfTheRoom()
    {
        return lengthOfTheRoom;
    }

    int GetNumberOfTabels()
    {
        return numberOfTabels;
    }

    int GetNumberOfChair()
    {
        return numberOfChair;
    }

    int GetNumberOfComputer()
    {
        return numberOfComputer;
    }

    int GetNumberOfPhone()
    {
        return numberOfPhone;
    }

    int GetNumberOfFamilyMembers()
    {
        return numberOfFamilyMembers;
    }

    int GetNumberOfAc()
    {
        return numberOfAc;
    }

    int GetNumberOfTubeLight()
    {
        return numberOfTubeLight;
    }
    int GetNumberOfBooks()
    {
        return numberOfBooks;
    }

    int GetNumberOfWindos()
    {
        return numberOfWindos;
    }

    int GetNumberOfDoors()
    {
        return numberOfDoors;
    }

    // add
    void AddNumberOfTabels(){
        numberOfTabels+=1;
    }


    // sub


    // change

    void ChangeNumberOfFans(int value)
    {
        SetNumberOfFans(value);
    }

    void ChangeNumberOfRooms(int value)
    {
        SetNumberOfRooms(value);
    }

    void ChangeBreathOfTheRoom(int value)
    {
        SetBreathOfTheRoom(value);
    }

    void ChangeLengthOfTheRoom(int value)
    {
        SetLengthOfTheRoom(value);
    }

    void ChangeNumberOfTabels(int value)
    {
        SetNumberOfTabels(value);
    }

    void ChangeNumberOfChair(int value)
    {
        SetNumberOfChair(value);
    }

    void ChangeNumberOfComputer(int value)
    {
        SetNumberOfComputer(value);
    }

    void ChangeNumberOfPhone(int value)
    {
        SetNumberOfPhone(value);
    }

    void ChangeNumberOfFamilyMembers(int value)
    {
        SetNumberOfFamilyMembers(value);
    }

    void ChangeNumberOfAc(int value)
    {
        SetNumberOfAc(value);
    }

    void ChangeNumberOfTubeLight(int value)
    {
        SetNumberOfTubeLight(value);
    }

    void ChangeNumberOfBooks(int value)
    {
        SetNumberOfBooks(value);
    }

    void ChangeNumberOfWindos(int value)
    {
        SetNumberOfWindos(value);
    }

    void ChangeNumberOfDoors(int value)
    {
        SetNumberOfDoors(value);
    }

    void info()
    {
        cout << "Number Of Rooms : " << GetNumberOfRooms() << endl;
        cout << "Breath Of The Room : " << GetBreathOfTheRoom() << endl;
        cout << "Length of the room : " << GetBreathOfTheRoom() << endl;
        cout << "Number Of Fans : " << GetNumberOfFans() << endl;
        cout << "Number Of Table : " << GetNumberOfTabels() << endl;
        cout << "Number Of Chair : " << GetNumberOfChair() << endl;
        cout << "Number Of Computer : " << GetNumberOfComputer() << endl;
        cout << "Number Of Phone : " << GetNumberOfPhone() << endl;
        cout << "Number Of Family Members : " << GetNumberOfFamilyMembers() << endl;
        cout << "Number Of Ac : " << GetNumberOfAc() << endl;
        cout << "Number Of TubeLight : " << GetNumberOfTubeLight() << endl;
        cout << "Number Of Books : " << GetNumberOfBooks() << endl;
        cout << "Number Of Windos : " << GetNumberOfWindos() << endl;
        cout << "Number Of Doors : " << GetNumberOfDoors() << endl;
    }
};

template <typename PrintType>
class Print
{
private:
public:
    Print(PrintType value)
    {
        cout << value << endl;
    }
};

class GetDayOfWeek
{
public:
    GetDayOfWeek(int dayNum)
    {
        string dayName = "";

        switch (dayNum)
        {
        case 0:
            dayName = "Sunday";
            break;

        case 1:
            dayName = "Monday";
            break;

        case 2:
            dayName = "Tuesday";
            break;

        case 3:
            dayName = "Wednesday";
            break;

        case 4:
            dayName = "Thursday";
            break;

        case 5:
            dayName = "Friday";
            break;

        case 6:
            dayName = "saturday";
            break;

        default:
            dayName = "Invalid day number";
            cout << "please enter the number from 0 to 7" << endl;
            break;
        }

        cout << "Day Name : " << dayName << endl;
    }
};

#endif // JoelJebitto_H
