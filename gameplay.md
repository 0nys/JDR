# Le JDR - Mécaniques de jeu

## Règles officielles

### Ce que les joueurs doivent savoir

+ Les joueurs choisissent au départ chacun un personnage.
	+ Chaque personnage possède une fiche de lore secret.
	+ Chaque personnage possède des capacités spéciales (secrètes) modifiant les règles du jeu.
	+ Chaque personnage possède un nombre de HP max initiaux et a initialement autant de HP
+ Les joueurs possèdent chacun un deck de cartes et deux bras, et jouent chacun leur tour.
+ À son tour, un joueur :
	+ joue les cartes qu'il veut de sa main dans l'ordre qu'il veut
	+ dispose d'un effet "action" gratuit par tour
	+ puis défausse autant de cartes qu'il veut de sa main
	+ si le joueur a moins de 4 cartes en main, il en repioche jusqu'à en avoir 4
	+ si la pioche est vide, la défausse est mélangée et devient la pioche
	+ si le joueur possède plus de 6 cartes en main il doit défausser des cartes jusqu'à en avoir 6
	+ Les cartes *réaction* peuvent être jouées hors de son tour, en réaction à un événement
+ Lors de son tour, un joueur peut également défausser un équipement équipé, le jetter au sol,
  ou le donner à un personnage dans la même case (qui l'équipe, le défausse ou le jette)
+ Les types de cartes :
	+ Déplacement : Déplace le personnage dans une case adjacente. Sortir de la case d'une entité agressive coûte 2 déplacements
	+ Action : Active un équipement équipé, ou réalise une action raisonnable au choix du joueur.
	  Le MJ est juge de ce qui doit être considéré comme une action
	+ Défense (réaction) : bloque tous les dégâts et effets d'une attaque visant ce joueur
	+ Équipement : équipe l'item dans un des bras / jette l'item au sol.
	  Certains équipements requièrent deux bras pour être équipés (cf `items.md`)
	+ Soin : les soins ont un nombre d'utilisations limité.
	  Utiliser un soin consomme autant d'utilisations que souhaité
	+ Sort : applique l'effet indiqué (cf `spells.md`)
	+ Blessure : aucun effet
+ Lorsqu'un personnage subit un dégât, il perd 1 HP et récupère dans sa défausse une carte blessure.
  Si un personnage est réduit à 0 HP, il meurt.


### Règles à donner ou non aux joueurs, suivant le niveau de mystère dans lequel ils veulent rester

+ Effet action :
	+ Ramasser un objet (y compris sel) n'est pas une action
	+ Lancer un équipement : applique l'effet de l'équipement avec le modificateur "distance", et l'équipement arrive sur sa cible
	+ Coup de poing : si utilisé sur une entité, l'entité pioche une carte. Si la carte a un effet, défend l'attaque, sinon applique 1 phys.
+ Les joueurs peuvent dire ce qu'ils veulent aux autres mais ne peuvent montrer ni leurs informations personnelles ni leur main.
+ Effets et modificateurs principaux :
	+ Par défaut tous les effets sont appliqués dans la case du personnage, à l'entité de son choix (ça peut être lui-même)
	+ **Physique X** : dégâts physiques. Inflige X dégâts.
	+ **Feu X** : dégâts de feu. Inflige X dégâts et applique l'effet *enflammé* pendant 1 tour.
	  Si la cible était gelée, la cible subit 2*(nombre de gel) dégâts de feu et perd son gel
	  (s'il s'agissait d'un personnage, il repioche autant de cartes)
	  Si la cible est mouillée, elle ne subit pas l'effet *enflammé*
	+ **Glace X** : Aucun dégât. Si appliqué à un personnage, fait défausser X cartes aléatoires.
	  Si appliqué à une entité non personnage, l'entité joue X cartes de moins (minimum 1) pendant 1 tour
	  Si la cible était enflammée, elle perd son effet enflammé et subit X dégâts de gel
	  Si la cible était mouillée, elle perd son effet mouillé et subit 1 dégât de gel
	+ **Électricité X** : dégâts électriques. Inflige X dégâts et X paralysie.
	  Si la cible est mouillée, elle subit 1 dégât de plus
	+ **Paralysie X** : à son prochain tour, doit utiliser X déplacements supplémentaires avant de pouvoir se déplacer
	+ **Soin X** : la cible récupère X HP (dans la limite de ses HP max).
	  Si la cible est un personnage, ce dernier peut supprimer jusqu'à X cartes blessure de sa défausse
	+ **Vent** : Crée une bourrasque qui pousse la cible dans la case adjacente de son choix, ou contre un mur pour 1 dégât physique
	  Peut être utilisé contre un mur, ce qui pousse le lanceur vers la case opposée au mur
	+ **Eau** : Supprime l'effet enflammé, applique l'effet mouillé pendant 1 tour
	+ **Distance** (modificateur) : L'effet modifié peut être appliqué à une case adjacente (orthogonale ou diagonale)
	+ **Multi** (modificateur) : L'effet modifié peut être appliqué à plusieurs cibles de la même case, au choix du lanceur de l'effet
	+ **Tous** (modificateur) : L'effet modifié est appliqué à toutes les cibles de la case
+ Lorsqu'un personnage meurt :
	+ Il laisse tomber tous ses équipements et soins au sol
	+ Il supprime toutes les blessures de son deck
	+ À tout moment le joueur peut décider de ressusciter.
	  Il apparaît alors à un endroit choisi par le MJ et réduit ses HP max au nombre initial divisé par 2^(le nombre de fois qu'il est mort)


### Détails et règles supplémentaires (surtout pour le MJ)

+ Lorsqu'une entité non personnage est activée (lorsqu'elle est susceptible d'agir), son tour de jeu est inséré après le joueur courant
+ Les effets de cartes doivent être appliqués en entier avant toute autre pose de carte
+ Vision des personnages :
	+ Les personnages ont une vision en ligne droite.
	+ À 0 et 1 case : ils voient parfaitement bien
	+ À 2 cases : ils ont un aperçu du contenu, forme de la case et issues
	+ À 3 cases : très vague aperçu (vide ou non), issues de la case
	+ Au-dela : rien
	+ Dans le noir : aperçu du contenu, forme de la salle et issues
+ Fonctionnement des entités non personnage :
	+ Chaque entité possède un nombre de HP, un nombre d'actions et un deck.
	+ À son tour, l'entité pioche son nombre d'actions en cartes de son deck et les joue dans l'ordre :
		+ Cartes rien : aucun effet (le MJ invente une action inutile)
		+ Autres cartes : si l'effet peut être appliqué à une cible cohérente avec les intentions de l'entité, elle le fait.
		  Sinon, l'entité se déplace (si possible) d'une case en direction du personnage après qui elle en veut le plus
	+ Les entités sont plus ou moins agressives envers les joueurs, et peuvent avoir des intentions variables.
	  Lorsqu'un joueur s'éloigne trop, l'entité est désactivée
	+ Ces règles ne sont que des guides, la priorité est que l'entité ait un comportement cohérent
	+ Lorsque l'entité perd tous ses HP elle meurt et son drop apparaît.
+ Effets des cristaux de sel :
	+ Noir : +2hp max ou +1hp max + soin 1
	+ Rouge : +5HP ou -5 blessures
	+ Jaune : Détruire 2 cartes de la main ou défausse
	+ Bleu : Tirer trois sorts au hasard (parmi les sorts tier 1 et 2), en choisir un parmi les trois
	+ Vert : Attaque perçante 4 à une entité de la case
	+ Violet : Améliore une carte de la main ou défausse
	+ Cyan (n'apparaît pas) : invoque un élémentaire de sel de couleur aléatoire
		+ Particularités : si vert, drop cristal vert à sa mort
		+ Stratégie : suit son invocateur et l'imite
		+ HP : 8 (12 si noir)
		+ Actions : 1
		+ Cartes : rien (3) (aucun si jaune), attaque 1 (3) (attaque 2 si violet), soin 1 si rouge, électricité 1 distance si bleu, gel si bleu
	+ Blanc : Choisir une couleur (si la couleur n'existe pas, est assaisonné)
	+ Si utilisé par Kaarvel, améliore également une carte au hasard (pioche)
+ Amélioration de cartes : le sel violet permet d'améliorer une carte. Les améliorations fonctionnent de la façon suivante :
	+ Soin X : soin X + 2
	+ Blessure : soin 1
	+ Équipement : ajoute/améliore un effet cohérent à l'équipement, au jugé du MJ
	+ Sort : sort équivalent du tier supérieur (s'il n'en existe pas, en prendre un cohérent)
	+ Défense : défense + action (toujours en réaction)
	+ Déplacement : +1 déplacement ou pioche 1 (équiprobable)
	+ Action : +1 action ou pioche 1 (équiprobable)
	+ Cartes non améliorables : sorts tier 3, équipements clef, bombe


## Fonctionnement du monde

+ Au bout d'un nombre de tours fixé, les cloches sonnent, la terre tremble et les brèches se referment
  Cet événement bloque les quêtes d'Anacron et de Karvel.
  Si des personnages de joueurs sont encore à l'extérieur à ce moment, attendre qu'ils reviennent pour fermer définitivement
  C'est cet événement qui doit motiver les joueurs à descendre et aller au-dela de leur quête personnelle
+ Chaîne logique du True Ending :
	+ 1er étage  : poster œil, œil noir -> poster dessins éléments
	+ 2ème étage : dessins éléments -> fragments de clef noire -> clef noire
	+ 3ème étage : serrure noire -> poster directions
	+ 4ème étage : directions -> pinceau
	+ 3ème étage : tableau 8ème patte -> indication dessin
	+ pyramide   : dessin sablier sur la tablette centrale -> Wuti
