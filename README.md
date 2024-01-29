# IDEA : Colision manager.

Actualy only the ball as a colision system that take into accont :
  - the Wall.colide function.
  - The boat position.
  - The window.

I need a drop item colision manager.
And a Bullet system colision manager.
An invader colision system manager.

|       | Window top    | Window Bottom | Window side | Ball         | Brick    | Boat      | Bullet | Invader | Drop |
|-------|------------   |---------------|-------------|--------------|----------|-----------|--------|---------|------|
|Ball   |Bounce Y miror | Lost          | Bounce X    | NA           | Give dmg |BounDirCtrl|NA      | S.Dmg   | NA   |
|Brick  |NA             | NA            | NA          | Take Damage  | NA       |NA         |smallDmg| NA      | NA   |
|Boat   |NA             | NA            | StopIt      |Bounce dirCtrl| NA       |NA         |takDmg  | NA      |TakeIt|
|Bullet |Lost           | Lost          | Lost        | NA           | Small dmg|Damage     |NA      | GivDmg  | NA   |
|Invader|Inv lost HP    | NA            | StopIt      | Small dmg    | NA       |NA         |TakDmg  | NA      | NA   |
|Drop   |(wait gravity) | Lost          | Bonce X     | NA           | NA       |TakeIt     |NA      | NA      | NA   |


 # Rules 1 - only active part take colide functions.

list of active parts :
 - Ball (by help of wall system ?)
 - Bullet
 - Boat

 Improve itemList for take into account :
  - Balls 
  - Bullets
  - Drops (already done)
Then Wall, invaders system and boat system use this itemList to detect colide with an item.

Each item in itemList will implement (for update) :
 - Colide top
 - Colide bottom
 - Colide wall(for bricks interractions)
 - Colide boat
 - Colide Invasion.
If not colide function will just return None.