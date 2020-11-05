/*********************************************
 * OPL 12.10.0.0 Model
 * Author: vu
 * Creation Date: Nov 3, 2020 at 10:42:13 AM
 *********************************************/

int n = ...; 
range I = 1..n;
int C[I][I] = ...;
 
// Generation des indices sous-graphes
/*{int} s= asSet(I);
range r=1 ..(ftoi(pow(2,card(s)))-1); // -1 pour eliminer {}
{int} iSousGraphes [k in r] = {i | i in s: ((k div (ftoi(pow(2,(ord(s,i))))) mod 2) == 1)};
*/
// Decision variable
dvar boolean X[I][I];
dvar float+ u[I]; // ranking vector

// Objective
minimize 
	sum(i in I) sum(j in I) C[i][j]*X[i][j];
	
subject to
{
  //forall (i in I) X[i][i] == 0;
  
  forall(j in I)
    sum(i in I : i != j) X[i][j] == 1;
  
  forall(i in I)
    sum(j in I : i != j) X[i][j] == 1;

  forall (i, j in I : j != 1) u[i] + X[i][j] <= u[j] + (n - 1) * (1 - X[i][j]);
  u[1] == 0; // Init l'ordre du premier sommet
  
  /*forall(ir in r) 
  	sum(i in iSousGraphes[ir]) sum(j in iSousGraphes[ir]) X[i][j] <= card(iSousGraphes[ir]) - 1;*/
  	
}

execute afficher{
  for(var i in I) {
    for(var j in I) {
      if (X[i][j] > 0) write(i, "->", j, "\n");
    }      
  }    
}  