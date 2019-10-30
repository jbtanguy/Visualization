generate_venn.py
================

Pour utiliser le programme evaluate.py, il faut disposer de :
- nombre de dimensions souhaitées dans pour le diagramme de Venn ;
- les chemins d'accès aux modèles contenant les résultats des modèles (instance  label)
- les noms des modèles à afficher sur le diagramme 
- le caracètre de séparation des instances dans les fichiers contenant les résultats des modèles
- le label que l'on souhaite représenter

Par exemple : ```python3 generate_venn.py "./models/m1.txt,./models/m2.txt,./models/m3.txt" "Model 1, Model 2, Model 3" \\t 1```
(Ici, le caractère de séparation est une tabulation et le label est "1".)

Ce code nécessite la présence de venn.py dans le même répertoire. Ce programme a été trouvé ici : https://github.com/tctianchi/pyvenn/blob/master/venn.py.

generate_upset_plot.py
======================

Pour utiliser le programme generate_upset_plot.py, il suffit de disposer de :
- les chemins d'accès aux modèles contenant les résultats des modèles (instance  label)
- le caracètre de séparation des instances dans les fichiers contenant les résultats des modèles
- l'indice de l'identifiant des instances dans les fichiers contenant les résultats modèles
- l'indice des labels dans les fichiers contenant les résultats modèles

Par exemple : ```python3 generate_upset_plot.py "model1.txt,model2.txt,modele3.txt,reference.txt" \\t 0 1``` (Ici, le caractère de séparation est une tabulation, l'indice des instances est "0" et l'indice des labels est "1"). 