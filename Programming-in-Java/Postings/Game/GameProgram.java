import java.util.ArrayList;

import javax.lang.model.util.ElementScanner6;

/*
Med hjälp av koden nedanför skall du skriva en metod som heter searchWeapo, denna metod ska ta in ett parameter argument
som motsvarar vapnet man vill söka på.
I metoden skall du med hjälp av en Switch sats ta reda på vem som bär vilket vapen.

Om inget vapen hittas så skall ett default meddelande skrivas ut.

För betyget VG:
Skriv en metod som utrustar valfri karaktär med vapnet "Excalibur". Se till att anropa denna metod på karaktären.
*/

public class GameProgram {

    String _characterName;
    String _weaponName;
    int _weaponDamage;
    int _hp;
    static int hammerMaximumDamage = 50;
    static int hammerMinimumDamage = 10;

    static int hammer = (int) (Math.random() * ((hammerMaximumDamage - hammerMinimumDamage) + 1)) + hammerMinimumDamage;
    static int magicWandMaximumDamage = 100;
    static int magicWandMinimumDamage = 0;
    static int magicWand = (int) (Math.random() * (magicWandMaximumDamage - magicWandMinimumDamage));

    public GameProgram(String charName, int wDamage, int health, String wName) {
        _characterName = charName;
        _weaponName = wName;
        _weaponDamage = wDamage;
        _hp = health;
    }

    public void beingAttacked(String defenderName, String attackerName, int attackerWeaponDamage,
            String attackerWeaponName) {
        if (_hp <= 0 || attackerWeaponName == "Excalibur") {
            System.err.println("YOU CANNOT ATTACK");
        } else {
            /* System.err.println("WILD " + attackerName + " APPEARS!"); */
            System.out.println(attackerName + " STRIKES " + defenderName + " WITH A " + attackerWeaponName + " IT DOES "
                    + attackerWeaponDamage + " DAMAGE");
            _hp = (_hp - attackerWeaponDamage);
            System.out.println(defenderName + " HAS " + _hp + " REMAINING HEALTH! ");
        }
    }

    public void searchWeapon(String wName) {
        switch (wName) {
            case "Hammer":
                if (_weaponName.equals(wName))
                    System.out.println("The \"" + wName + "\" weapon is used by: " + _characterName);
                else
                    System.out.println("The \"" + wName + "\" weapon is NOT used by: " + _characterName);
                break;

            case "Magic Wand":
                if (_weaponName.equals(wName))
                    System.out.println("The \"" + wName + "\" weapon is used by: " + _characterName);
                else
                    System.out.println("The \"" + wName + "\" weapon is NOT used by: " + _characterName);

                break;

            case "Excalibur":
                if (_weaponName.equals(wName))
                    System.out.println("The \"" + wName + "\" weapon is used by: " + _characterName);
                else
                    System.out.println("The \"" + wName + "\" weapon is NOT used by: " + _characterName);
                break;

            default:
                System.out.println("The weapon \"" + wName + "\" not found!");
                System.out.println("No valid weapon found for the character \"" + _characterName + "\"");
                break;
        }
    }

    public void drinkingHealingPotion() {
        int healingPotion = 20;
        _hp = _hp + healingPotion;
        System.out.println(_characterName + " GAINED " + healingPotion + " HEALTH BY DRINKING A HEALING POTION");
        System.out.println(_characterName + " NOW HAS A HEALTH OF " + _hp);
    }

    // Method to change weapon
    public void changeWeapon(String newWeapon) {
        _weaponName = newWeapon;
        System.out.println("The character \"" + _characterName + "\" now has an " + _weaponName + " weapon!");
    }

    public static void main(String[] args) {
        GameProgram goodGuy = new GameProgram("The Beast", hammer, 100, "Hammer");
        GameProgram evilGuy = new GameProgram("Jafar", magicWand, 80, "Magic Wand");
        GameProgram oddGuy = new GameProgram("Odd Guy", magicWand, 60, "Unarmed");

        goodGuy.beingAttacked(goodGuy._characterName, evilGuy._characterName, evilGuy._weaponDamage,
                evilGuy._weaponName);
        evilGuy.beingAttacked(evilGuy._characterName, goodGuy._characterName, goodGuy._weaponDamage,
                goodGuy._weaponName);
        // goodGuy.drinkingHealingPotion();
        // evilGuy.drinkingHealingPotion();

        System.out.println("\n===== Added output =====");
        goodGuy.searchWeapon("Hammer");
        evilGuy.searchWeapon("Hammer");
        oddGuy.searchWeapon("A stick");

        // Change to a new weapon
        goodGuy.changeWeapon("Excalibur");
    }
}