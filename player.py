import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, xcoor, ycoor, team, spec, sprites, all_projectiles, lsbullets, bullets, bigassbullets,
                 punyassbullets):
        pygame.sprite.Sprite.__init__(self)
        self.res = pygame.display.get_surface().get_size()
        self.x = xcoor
        self.y = ycoor
        self.team = team
        # projectiles
        self.allprojectiles = pygame.sprite.Group()
        self.bullets = bullets
        self.lsbullets = lsbullets
        self.bigassbullets = bigassbullets
        self.punyassbullets = punyassbullets
        #statistics
        self.number_of_shots = 0  # number of bullets shot by player
        self.number_of_hits = 0  # bullets hit
        self.manaspent = 0
        self.damagetaken=0
        self.hp=0
        self.image = pygame.image.load("assets/" + spec + team.lower() + ".png")
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.sprites = sprites
        self.res = 800, 600
        # spec stuff
        self.spec = spec
        if self.spec == "spec1":  # lifesteal
            self.maxhp = 250
            self.hp = self.maxhp
            self.mana = 100
            self.vel = 10
            if self.team == "BLUE":
                self.imagefile = "assets/spec1blue.png"
            elif self.team == "RED":
                self.imagefile = "assets/spec1red.png"
        elif self.spec == "spec2":  # rocket launcher
            self.maxhp = 375
            self.hp = self.maxhp
            self.mana = 100
            self.vel = 7
            if self.team == "BLUE":
                self.imagefile = "assets/spec2blue.png"
            elif self.team == "RED":
                self.imagefile = "assets/spec2red.png"
        elif self.spec == "spec3":  # machine gun
            self.maxhp = 250
            self.hp = self.maxhp
            self.mana = 100
            self.vel = 13
            if self.team == "BLUE":
                self.imagefile = "assets/spec3blue.png"
            elif self.team == "RED":
                self.imagefile = "assets/spec3red.png"
        # statistics (also end health, spec)
        self.number_of_shots = 0  # number of bullets shot by player
        self.number_of_hits = 0  # bullets hit
        self.accuracy = 0
        self.manaspent = 0
        self.damagetaken = 0

    def specialAbility1(self):  # lifesteal
        if self.mana >= 10:
            lsbullet = Projectile(self.x, self.y, 5, 10, self.team, "assets/spec1special.png")
            self.allprojectiles.add(lsbullet)
            self.lsbullets.add(lsbullet)
            self.sprites.add(lsbullet)
            self.mana -= 10
            self.manaspent + 10
            return True

    def specialAbility2(self):  # rocket launcher
        if self.mana >= 20:
            if self.team == 'BLUE':
                bigassbullet = Projectile(self.x, self.y, 2.5, 25, self.team, "assets/Rocket(blue).png")
            if self.team == 'RED':
                bigassbullet = Projectile(self.x, self.y, 2.5, 25, self.team, "assets/Rocket(red).png")
            self.allprojectiles.add(bigassbullet)
            self.bigassbullets.add(bigassbullet)
            self.sprites.add(bigassbullet)
            self.mana -= 20
            self.manaspent += 20
            return True

    def specialAbility3(self):  # machine gun
        if self.mana >= 5:
            punyassbullet = Projectile(self.x, self.y, 10, 5, self.team, "assets/spec3special.png")
            self.allprojectiles.add(punyassbullet)
            self.punyassbullets.add(punyassbullet)
            self.sprites.add(punyassbullet)
            self.mana -= 3
            self.manaspent += 3
            return True

    def updoot(self, number_of_hits, event, keys):
        self.number_of_hits = number_of_hits
        if event.type == pygame.KEYDOWN:
            if self.team == "BLUE":
                if keys[pygame.K_w]:
                    self.y -= self.vel
                if keys[pygame.K_a]:
                    self.x -= self.vel
                if keys[pygame.K_s]:
                    self.y += self.vel
                if keys[pygame.K_d]:
                    self.x += self.vel
                if keys[pygame.K_q]:
                    if self.mana >= 1:
                        bullet = Projectile(self.x, self.y, 5, 10, self.team, "assets/bullet.png")
                        self.allprojectiles.add(bullet)
                        self.bullets.add(bullet)
                        self.sprites.add(bullet)
                        self.mana -= 1
                        self.manaspent += 1
                        self.number_of_shots += 1
                if keys[pygame.K_e]:
                    if self.spec == "spec1":
                        didShoot = self.specialAbility1()
                        if didShoot:
                            self.number_of_shots += 1
                    elif self.spec == "spec2":
                        didShoot = self.specialAbility2()
                        if didShoot:
                            self.number_of_shots += 1
                    elif self.spec == "spec3":
                        didShoot = self.specialAbility3()
                        if didShoot:
                            self.number_of_shots += 1
                if self.x < 0:  # BLUE stay inbounds x
                    self.x = 0
                if self.x > self.res[0] / 2:
                    self.x = self.res[0] / 2

        if self.team == "RED":
            if keys[pygame.K_i]:
                self.y -= self.vel
            if keys[pygame.K_j]:
                self.x -= self.vel
            if keys[pygame.K_k]:
                self.y += self.vel
            if keys[pygame.K_l]:
                self.x += self.vel
            if keys[pygame.K_u]:
                if self.mana >= 1:
                    bullet = Projectile(self.x, self.y, 10, 10, self.team, "assets/bullet.png")
                    self.allprojectiles.add(bullet)
                    self.bullets.add(bullet)
                    self.sprites.add(bullet)
                    self.mana -= 1
                    self.number_of_shots += 1
            if keys[pygame.K_o]:
                if self.spec == "spec1":
                    didShoot = self.specialAbility1()
                    if didShoot:
                        self.number_of_shots += 1
                if keys[pygame.K_o]:
                    if self.spec == "spec1":
                        didShoot = self.specialAbility1()
                        if didShoot:
                            self.number_of_shots += 1
                    elif self.spec == "spec2":
                        didShoot = self.specialAbility2()
                        if didShoot:
                            self.number_of_shots += 1
                    elif self.spec == "spec3":
                        didShoot = self.specialAbility3()
                        if didShoot:
                            self.number_of_shots += 1
            if self.x < self.res[0] / 2:  # RED stay inbounds x
                self.x = self.res[0] / 2
            if self.x > self.res[0]:
                self.x = self.res[0]
        if self.y < 0:  # BOTH stay inbounds y
            self.y = 0
        if self.y > self.res[1]:
            self.y = self.res[1]
            # if len(self.bullets.sprites()) > 0:
            #     for bullet in self.bullets:
            #         self.number_of_hits = bullet.bullet_travelling(enemy_player, self.number_of_hits)

            # if projectile[bullet].hitstat:
            #     damagetaken +=projectile[bullet].dmg
        if self.number_of_shots > 0:
            self.accuracy = int(self.number_of_hits) / int(self.number_of_shots)
        self.rect.center = self.x, self.y
