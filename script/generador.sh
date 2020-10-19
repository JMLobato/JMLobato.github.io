#!/bin/bash
echo "Rellena el formulario para generar una página web nueva: "
for linea in $(cat plantilla.txt)
	do 
		if [ $linea != "texto" ]
			then
				read -p "$linea" tmp
				echo "$linea $tmp" >> tmp.txt
			else
				read -p "¿Quieres añadir algo más? s/n: " respuesta
				if [ respuesta == "s" ]
					then
						nano tmp.txt
					else
						echo "Okay, finalizando pues..."
				fi	
		fi
	done
cp tmp.txt ../content/prueba.md
git add --all
git commit -m "añadido automatico"
git push
pelican content
pelican --listen