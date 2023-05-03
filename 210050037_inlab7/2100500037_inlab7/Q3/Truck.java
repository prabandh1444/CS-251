package Q3 ;

/*
 * TODO: Create class Truck along with proper methods and inheritance as required
 */
public class Truck extends Vehicle
{
  public Truck(String r,String m,String o){
    this.regNo = r;
    this.manufacturer = m;
    this.owner = o;
    this.pollutionStatus="PENDING";
  }
  public void checkPollutionStatus(){
    if(CO2 > 25 || CO > 0.8 || HC > 1000){
        this.pollutionStatus="FAIL";
    }
    else
        this.pollutionStatus="PASS";
  }
  public String toString(){
    String s;
    s="Reg No: "+ regNo +"\n" + "Manufacturer: "+ manufacturer +"\n"+
    "Owner: "+ owner +"\n"+
    "Pollution Status: "+pollutionStatus+"\n";
    return s;
  }
}