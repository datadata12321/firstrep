#include<iostream>

class rlvalues 
{
public:
    rlvalues(): number(new int[5]()) {
        for (int i = 0; i < 5; i++) {
            number[i] = i+1;
        }
    }

    ~rlvalues() 
    { 
        std::cout << "destroyed" << std::endl;
        delete[] number;    
    }
    
    rlvalues(rlvalues&& re): number(re.number)
    {
        std::cout << "what is it?" << std::endl;
    }

    rlvalues& operator= (rlvalues&& again)
    {
        std::cout << "then what is this?" << std::endl;
        number = again.number;
        again.number = nullptr;
        return *this;
    }
private:
    int * number = nullptr;
};


rlvalues func() {
    rlvalues rl;
    return std::move(rl);
}
        
int main() {

    rlvalues d = func();
    return 0;
}