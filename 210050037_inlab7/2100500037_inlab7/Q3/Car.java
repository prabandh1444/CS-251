package Q3 ;

/*
 * TODO: Create class Car along with proper methods and inheritance as required
 */
public class Car extends Vehicle
{
  public Car(String r,String m,String o){
    this.regNo = r;
    this.manufacturer = m;
    this.owner = o;
    this.pollutionStatus="PENDING";
  }
  public void checkPollutionStatus(){
    if(CO2 > 15 || CO > 0.5 || HC > 750){
        this.pollutionStatus="FAIL";
    }
    else
        this.pollutionStatus="PASS";
  }
  public   String toString(){
    String s;
    s="Reg No: "+ this.regNo +"\n" + "Manufacturer: "+ manufacturer +"\n"+
    "Owner: "+ this.owner +"\n"+
    "Pollution Status: "+this.pollutionStatus+"\n";
    return s;
  }
}