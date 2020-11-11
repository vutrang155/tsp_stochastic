/*********************************************
 * OPL 12.10.0.0 Model
 * Author: vu
 * Creation Date: Nov 3, 2020 at 10:42:13 AM
 *********************************************/

int n = ...; 
range I = 1..n;
float C[I][I] = ...;
float alpha = ...;
float taux_majoration = ...;
float quantileF[I][I];
float V[I][I];

execute getVmatrix{
    for (var i in I){
        for (var j in I){
            if (i==j) 
                {V[i][j]=0}
            if (i>j)
                {
                    V[i][j]=Math.random()*C[i][j];
                    V[j][i]=V[i][j];
                }
        }
    }
}

execute quantile {
	for (var i in I){
        for (var j in I){
           //quantileF[i][j] = C[i][j] + V[i][j] * (sqrt(3)/Math.PI) * ln(alpha/(1-alpha));

           quantileF[i][j] = C[i][j] + (V[i][j] * (Math.sqrt(3)/Math.PI) * Math.log(alpha/(1-alpha)));
        }
    }
} 
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
  
  // 4e contrainte
  sum(i in I) sum(j in I) X[i][j]*quantileF[i][j] <= 7544.36590190409*(1+taux_majoration);
  //sum(i in I) sum(j in I) X[i][j]*quantileF[i][j] <= sum(i in I) sum(j in I) X[i][j]*C[i][j]* (1+taux_majoration);
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