class Combat:
    def __init__(self,player_Pokemon,attack,life1,defense,chance,type,player,ops_Pokemon,win):
        self.player_pokemon=player_Pokemon
        self.ops_pokemon=ops_Pokemon
        self.attack= attack
        self.life1= life1
        self.defense=defense
        self.chance=chance
        self.type= type
        self.player=player
        self.win= win 
        win=False


    def type_puissance(self,type1,type2):

        types = [
        "Normal", "Combat", "Vol", "Poison", "Sol", "Roche",
        "Insecte", "Spectre", "Acier", "Feu", "Eau", "Plante",
        "Électrik", "Psy", "Glace", "Dragon", "Ténèbres", "Fée"
        ]


        matrice = [
        # Nor  Com  Vol  Poi  Sol  Roc  Ins  Spe  Aci  Feu  Eau  Pla  Ele  Psy  Gla  Dra  Ten  Fée  
        [ 1,   1,   1,   1,   1,  0.5,  1,   0,  0.5,  1,   1,   1,   1,   1,   1,   1,   1,   1 ],  # Normal
        [ 2,   1,  0.5, 0.5,  1,   2,  0.5,  0,   2,   1,   1,   1,   1,  0.5,  2,   1,   2,  0.5 ],  # Combat
        [ 1,   2,   1,   1,   1,  0.5,  2,   1,  0.5,  1,   1,   2,  0.5,  1,   1,   1,   1,   1 ],  # Vol
        [ 1,  0.5,  1,   1,  0.5, 0.5,  1,  0.5,  0,   1,   1,   2,   1,   1,   1,   1,   1,   2 ],  # Poison
        [ 1,   2,   0,   1,   1,   2,   1,   1,   2,   2,   1,  0.5,  2,  0.5,  1,   1,   1,   1 ],  # Sol
        [ 1,  0.5,  2,   1,  0.5,  1,   2,   1,  0.5,  2,   1,   1,   1,   1,   2,   1,   1,   1 ],  # Roche
        [ 1,  0.5, 0.5, 0.5,  1,   1,   1,  0.5, 0.5, 0.5,  1,   2,   1,   2,   1,   1,   2,  0.5 ],  # Insecte
        [ 0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1,   1,  0.5,  1 ],  # Spectre
        [ 1,   1,   1,   1,   1,   2,   1,   1,  0.5, 0.5, 0.5,  1,  0.5,  1,   2,  0.5,  1,   2 ],  # Acier
        [ 1,   1,   1,   1,   1,  0.5,  2,   1,   2,  0.5, 0.5,  2,   1,   1,   2,  0.5,  1,   1 ],  # Feu
        [ 1,   1,   1,   1,   2,   2,   1,   1,   1,   2,  0.5, 0.5,  1,   1,   1,  0.5,  1,   1 ],  # Eau
        [ 1,   1,  0.5, 0.5,  2,   2,  0.5,  1,  0.5, 0.5,  2,  0.5,  1,   1,   1,  0.5,  1,   1 ],  # Plante
        [ 1,   1,   2,   1,   0,   1,   1,   1,   1,   1,   2,  0.5, 0.5,  1,   1,  0.5,  1,   1 ],  # Électrik
        [ 1,   2,   1,   2,   1,   1,   1,   1,  0.5,  1,   1,   1,   1,  0.5,  1,   1,   0,   1 ],  # Psy
        [ 1,   1,   2,   1,   2,   1,   1,   1,  0.5, 0.5, 0.5,  2,   1,   1,  0.5,  2,   1,   1 ],  # Glace
        [ 1,   1,   1,   1,   1,   1,   1,   1,  0.5,  1,   1,   1,   1,   1,   1,   2,   1,   0 ],  # Dragon
        [ 1,  0.5,  1,   1,   1,   1,   1,   2,   1,   1,   1,   1,   1,   2,   1,   1,  0.5, 0.5 ],  # Ténèbres
        [ 1,   2,   1,  0.5,  1,   1,   1,   1,  0.5, 0.5,  1,   1,   1,   1,   1,   2,   2,   1 ],  # Fée
        ]
    
        i = types.index(type1)
        j = types.index(type2)
        power= matrice[i][j]
        pw_attack=self.attack*power
        return pw_attack
    def new_life(self,pw_attack,defense):
        damage= pw_attack-defense
        if damage<0:
            damage*(-1)
            new_life= self.life-damage
            self.life=new_life
            return self.life
        else:
            defense=damage         
    def winner_name(self):
        self.win = False
        if self.life1<=0:
            self.win = True
            return self.player,self.win
        elif self.life2<=0:
            self.win=True
            return self.ops_pokemon, self.win

    def pokemon_winner(self):
           self.win = False
        if self.life1<=0:
            self.win = True
            return self.player,self.win
        elif self.life2<=0:
            self.win=True
            return self.ops_pokemon, self.win


          
          
        
        
        

test= Combat(4,5,2,1,3,6)
print(test.type_puissance("Eau", "Feu")) 


