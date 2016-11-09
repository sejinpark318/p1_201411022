public class LeapYear{

    public void CalLeapYear(int year){
        if(((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) {
            System.out.println(year+"is leap year~!");
        }
        else{
            System.out.println(year+"is not leap year~!");
        }
    }
    
    public static void main(String[] args){
        LeapYear ly = new LeapYear();
        int[] years={1800,1900,1912,1984,1985,2000,2015,1825,1928,2031,1845,1947,2053,2099};
        for(int i:years){
            ly.CalLeapYear(i);
        }
        
    }

}