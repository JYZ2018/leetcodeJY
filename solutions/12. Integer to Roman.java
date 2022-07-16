class Solution {
    public String intToRoman(int num) {
        
        
//         int divider =1000;
//         StringBuilder str = new StringBuilder();
//         int sharp; int reminder;
//         while (divider>=1) {
//             sharp = num / divider;
//             reminder = num % divider;
//             if (divider==1000 && sharp>0 && reminder>=0 ) {
//                 if (sharp<5) str.append("M".repeat(sharp));
//             }
//            else if (divider==100 && sharp>0 && reminder>=0) {
//                if (sharp<4) str.append("C".repeat(sharp));
//                else if (sharp==4) str.append("CD");
//                else if (sharp==9) str.append("CM");
//                else if (sharp==5) str.append("D");
               
//                else {
//                    str.append("D");
//                    str.append("C".repeat(sharp-5));
//                 }
//            }   
//              else if (divider ==10 && sharp>0 && reminder>=0) {
//                if (sharp<4) str.append("X".repeat(sharp));
//                else if (sharp==4) str.append("XL");
//                else if (sharp==9) str.append("XC");
//                else if (sharp==5) str.append("L");
//                else {
//                    str.append("L");
//                    str.append("X".repeat(sharp-5));
//                  }
//              }    
//             else if  (divider==1 && sharp>0 && reminder==0) {
//                if (sharp<4) str.append("I".repeat(sharp));
//                else if (sharp==4) str.append("IV");
//                else if (sharp==9) str.append("IX");
//                else if (sharp==5) str.append("V");
//                else {
//                    str.append("V");
//                    str.append("I".repeat(sharp-5));
//             }
//             }           
//         divider = divider/10;
//            num= reminder; 
//         }
        
//         String res =str.toString();
//         return res;
        
    }
}
