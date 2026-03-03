# 🎮 Comment lancer le jeu Pokémon

## ✅ Dépendances installées
- Python 3.13.4 ✅
- pygame 2.6.1 ✅

## 🚀 Méthodes de lancement

### Option 1 : Double-cliquer sur le fichier batch
```
launch.bat
```
Double-cliquez simplement sur ce fichier pour lancer le jeu.

### Option 2 : Terminal avec chemin complet
```powershell
C:\Python313\python.exe interface.py
```

### Option 3 : Ajouter Python au PATH (recommandé)
1. Ouvrez les Paramètres Windows → Système → Paramètres système avancés
2. Variables d'environnement → PATH
3. Ajoutez : `C:\Python313` et `C:\Python313\Scripts`
4. Redémarrez le terminal
5. Ensuite vous pourrez utiliser :
```powershell
python interface.py
```

## 🎯 Contrôles du jeu

### Menu Principal
- **JOUER** → Lance la sélection de Pokémon puis le combat
- **POKÉDEX** → Voir tous les Pokémon capturés
- **QUITTER** → Fermer le jeu

### Combat
- **Clic sur "Attaquer"** → Attaque l'adversaire
- Le combat se termine quand un Pokémon atteint 0 PV

### Écran de victoire
- **ENTRÉE** ou **Clic sur "RETOUR AU MENU"** → Retour au menu

## 📊 Fonctionnalités
- ✅ Système de combat avec types et dégâts
- ✅ Gain d'XP et montée de niveau
- ✅ Évolution après 3+ combats ou niveau requis
- ✅ Pokédex avec sauvegarde automatique
- ✅ Écran de victoire/défaite
- ✅ Statistiques détaillées

## ⚠️ Note
Le warning sur `pkg_resources` est normal et n'affecte pas le jeu.
