class Solution {
public:
    string intToRoman(int num) {
        string currSym = "I";
        string midSym = "V";
        string nextSym = "X";
        string res ="",val;
        
        int temp ,temp2, place=1;
        
        while(num){
            temp = num%10;
            num= num/10;
            if(temp<=3){
                while(temp){
                    res = currSym + res;
                    temp--;
                }
            }
            else if(temp==4){
                res = currSym+midSym+res;
            }
            else if(temp>=5 && temp<=8){
                temp2 = temp-5;
                val = midSym;
                while(temp2){
                    val = val+currSym;
                    temp2--;
                }
                res= val+res;
            }
            else {
                res = currSym + nextSym+res;
            }
            
            place++;
            if(place == 2){
                currSym = nextSym;
                midSym = "L";
                nextSym="C";
                
            }else if(place == 3){
                currSym = nextSym;
                midSym = "D";
                nextSym="M";                
            }else{
                currSym = nextSym;
                midSym ="";
                nextSym="";
            }
        
        
    }
        return res;
    }
};