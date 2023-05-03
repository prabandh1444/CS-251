
function func() {

    console.log('Hi!');
      
      var arr=[];
  
              var Sports = document.getElementById("hobby1");
              if(Sports.checked){
                    arr.push(Sports.value);
             }
             else
              {
               document.getElementById('Sports').style.display='none';
               }
  
  
             var gaming = document.getElementById("hobby2");
              if(gaming.checked){
                    arr.push(gaming.value);
             }
              else
              {
               document.getElementById('gaming').style.display='none';
               }
  
  
               var reading = document.getElementById("hobby3");
               if( reading.checked){
                     arr.push(reading.value);
              }
               else
               {
                document.getElementById('reading').style.display='none';
                }
  
                var  streaming= document.getElementById("hobby4");
                if( streaming.checked){
                      arr.push(streaming.value);
               }
                else
                {
                 document.getElementById('streaming').style.display='none';
                 }
  
                 var music = document.getElementById("hobby5");
                 if( music.checked){
                       arr.push(music.value);
                }
                 else
                 {
                  document.getElementById('music').style.display='none';
                  }
  
  
               console.log(arr.length);
      
             if(arr.length<=0)
             { 
             arr.push("Please select atleast one Hobby")
             alert(arr);
             }
           
              else
             {
              alert("Your selected hobbies are "+arr);
               for(var i=0;i<arr.length;i++)
                {
                 document.getElementById(arr[i]).style.display='block';
                  }  
              }
               
  }