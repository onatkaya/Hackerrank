/*Write the class AddElements here*/
template<class T>
class AddElements
{
    private:
        T value;
    
    public:
        AddElements(T element1)
        {
            value = element1;
        }
        
    
        T add(T element2)
        {
            return element2 + value;
        }
};

template<>
class AddElements<string>
{
    private:
        string value;
        
    public:
        AddElements(string element1)
        {
            value = element1;
        }
        
        string concatenate(string element2)
        {
            return value.append(element2);
        }
};
