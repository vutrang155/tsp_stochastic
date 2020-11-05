/*********************************************
 * OPL 12.10.0.0 Model
 * Author: vu
 * Creation Date: Nov 3, 2020 at 10:42:13 AM
 *********************************************/

int n = ...; 
range I = 1..n;
float C[I][I] = ...;
 
// Decision variable
dvar boolean X[I][I];
dvar float+ u[I]; // ranking vector

// Objective
minimize 
	sum(i in I) sum(j in I) C[i][j]*X[i][j];
	
subject to
{
  forall(j in I)
    sum(i in I : i != j) X[i][j] == 1;
  
  forall(i in I)
    sum(j in I : i != j) X[i][j] == 1;

  forall (i, j in I : j != 1) u[i] + X[i][j] <= u[j] + (n - 1) * (1 - X[i][j]);
  u[1] == 0; // Init l'ordre du premier sommet
}


// Afficher le resultat 
range Ir = 0..n-1;
execute afficher{
  for(var i in Ir) {
  	for(var j in I) {
    	if(u[j] == i) {
    	  if (i != n-1) write(j,"\n"); 
    	  else write(j);
    	}
  	}
 }  	
  /*
  for(var i in I) {
    for(var j in I) {
      if (X[i][j] > 0) write(i, "->", j, "\n");
    }      
  } */
  

}  