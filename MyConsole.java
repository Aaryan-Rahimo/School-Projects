//Import Scanner tool
 
import java.util.Scanner;
public class MyConsole {
  public static void main(String[] args) {

    //Sets file name to genres.txt and reads through the file array
    FileReader myFileReader = new FileReader("genres.txt");
    String[] genres = myFileReader.getStringData(498);

    //Sets file name to artists.txt and reads through the file array
    myFileReader = new FileReader("artists.txt");
    String[] artists = myFileReader.getStringData(498);

    //Sets file name to albums.txt and reads through the file array
    myFileReader = new FileReader("albums.txt");
    String[] albums = myFileReader.getStringData(498);

    //Instantiate input object of scanner 
    Scanner input = new Scanner(System.in);

    //Instantiate mySpotbox object of Spotbox, with parameters of the text files
    Spotbox mySpotbox = new Spotbox(genres, artists, albums, "Untitled-1");

    //Create user choice, which will be changed later, allows program to loop
    String userChoice = "";
    
    /*
     * Creates while loop which containts and runs the entire user interactions 
     * This program is the brains of Spotbox, asking the user if they would like to explore genres or create a playlist
     * The loop will stop if the userChoice varriable is equal to quit
     */
    while (!userChoice.equalsIgnoreCase("Quit")) {

      System.out.println("Opening Spotbox....");
      //Welcomes user to the Spotbox program 
      System.out.println("---------------\\Welcome to Spotbox, the number 2 music platform in the World!/---------------");
      System.out.println("");
      //Displays options of explore music, create album or quit
      System.out.println("Explore Music (Enter Explore)");
      System.out.println("Create Playlist(Enter Create)");
      System.out.println("---------------------------------------------------------------------------------------------");

      //Prompts user to pick an option and states that typing quit will exit the program
      System.out.print("Which of the following would you like to choose (type quit to exit): ");

      //Creating array of valid options, which will be passed through a custom method
      String [] validStart = {"Create", "Explore", "Quit"};

      //Takes user input
      userChoice = input.nextLine();

      //Custom method will check if the user input is vaild in relation to the validStart array
      while (!mySpotbox.checkValid(userChoice, validStart)){
          //Displays error message, prompts and takes new user input
          System.out.print("That is an invalid option, please try again!: ");
          userChoice = input.nextLine();
      }

      //The code that will execute if the user would like to explore the music genres
      if(userChoice.equalsIgnoreCase("Explore")){

        //Asks user which genres they would like to explore
        System.out.println("-------------------Which of the following genres would you like to explore?------------------");
        
        //For loops will loops through the constant array of GENRE_LIST and will print each element
        for (String genre: mySpotbox.GENRE_LIST){
          System.out.println("-"+genre);
        }
        System.out.println("---------------------------------------------------------------------------------------------");
        
        //Prompts user to choose a genre 
        System.out.print("Please choose one of the genres listed: ");

        //Takes user input
        String userGenre = input.nextLine();

        //Custom method will check if the user input is vaild in relation to the GENRE_LIST array
        while (!mySpotbox.checkValid(userGenre, mySpotbox.GENRE_LIST)){

          //Displays error message, prompts and takes new user input
          System.out.print("That is an invalid option, please try again!: ");
          userGenre = input.nextLine();
        }

        //Assign varriable to value of genreCount
        int genreLength = mySpotbox.getGenreCount(userGenre);
        //Prints the number of albums within the genre 
        System.out.println("---------------------------------------------------------------------------------------------");
        System.out.println("\nThere are " + genreLength + " albums and artists in the " + userGenre + " genre.");
        System.out.println("\n---------------------------------------------------------------------------------------------");
        
        //Asks the user what they would like to further know about the genre
        System.out.println("Would you like to know top artists of the " + userGenre + " genre : ");
                
        //Prompts user to choose an option
        System.out.print("\nEnter Continue or Quit : ");        

        //Creating array of valid options, which will be passed through a custom method
        String[] validExplore = {"Continue", "Quit"};

        //Takes user input
        String exploreArtists = input.nextLine();

        //Custom method will check if the user input is vaild in relation to the validExplore array
        while (!mySpotbox.checkValid(exploreArtists, validExplore)){

            //Displays error message, prompts and takes new user input
            System.out.print("That is an invalid option, please try again!: ");
            exploreArtists = input.nextLine();
        }

        //The code that will execute if the user would like to explore Artists
        if (exploreArtists.equalsIgnoreCase("Continue")){
          System.out.println("---------------------------------------------------------------------------------------------");
          System.out.println("How many artists would you like to view in this genre?:");
          System.out.println("-All(enter " + genreLength +")");
          System.out.println("-5");
          System.out.println("-10");
          System.out.println("-15");
          System.out.println("-20");
          System.out.println("---------------------------------------------------------------------------------------------");

          //Prompts user to choose an option
          System.out.print("Please choose one of the given options: ");
          
          // Takes user input
          int numberView = input.nextInt();

          // Custom method will check if the user input is valid in relation to the numbers given
          while (numberView != 5 && numberView != 10 && numberView != 15 && 
          numberView != 20 && numberView != genreLength) {

            // Displays error message, prompts and takes new user input
            System.out.print("That is an invalid option, please try again!: ");
            numberView = input.nextInt();
          }
          
          //Creates new array that contains the artists from the genre, as well as the length
          String[] artistsList = mySpotbox.getArtists(userGenre, numberView);

          //Prints out Artists
          System.out.println("---------------------------------------------------------------------------------------------\n");
          int count = 0;
          for (String artist:artistsList){
            System.out.println(count+1+". "+artist);
            count++;
          }

          //Moves on to the next seciton with the albums
          System.out.println("\n----------------------------------------------------------------------------------------------");
          System.out.println("\nNow that we've looked into artists, lets explore albums!");

          //Reset input
          input.nextLine();

          //Asks user to choose Artist or input
          System.out.println("Would you like to view albums within the genre or by a specific artist?");
          System.out.println("- Artist");
          System.out.println("- Genre");
          System.out.print("Please Choose one of the options (quit to exit): ");

          //Creating array of valid options, which will be passed through a custom method
          String[] validExploreAlbums = {"Artist", "Genre", "Quit"};

          //Takes user input
          String exploreAlbums = input.nextLine();

          //Checks if user input is valid
          while(!mySpotbox.checkValid(exploreAlbums, validExploreAlbums)){

            // Displays error message, prompts and takes new user input
            System.out.print("That is an invalid option, please try again!: ");
            exploreArtists = input.nextLine();
          }
          
          System.out.println("\n----------------------------------------------------------------------------------------------");
          
          //If the user chooses artist, this code will run 
          if(exploreAlbums.equalsIgnoreCase("Artist")){

            //Asks user which artists they would want to see info on 
            System.out.print("Which artist would you like to see albums of?: ");

            //Takes user input 
            String userArtist = input.nextLine();

            //Checks if user input is valid in relation to artist list 
            while (!mySpotbox.checkValid(userArtist, artistsList)){

              // Displays error message, prompts and takes new user input
              System.out.println("That artist is no in the artist list!");
              System.out.print("Enter a valid option: ");
              userArtist = input.nextLine();
            }
           
            //Prints out artist albums
            System.out.println("---------------------------------------------------------------------------------------------\n");
            System.out.println(mySpotbox.getAlbums(userGenre, userArtist, mySpotbox.getArtistCount(userArtist), exploreAlbums));
            System.out.println("---------------------------------------------------------------------------------------------");
             
            //Asks user if they would like to continue using Spotbox or quit 
            System.out.println("Would you like to use Spotbox again?");
            System.out.print("Enter Continue or Quit: ");

            //Take user input
            userChoice = input.nextLine();

            //Checks if user input is valid or not
            while (!mySpotbox.checkValid(userChoice, validExplore)){

              //Displays error message, prompts and takes new user input
              System.out.print("That is an invalid option, please try again!: ");
              userChoice = input.nextLine();
            }

            //If the user enters quit, the program will display and an exit message and the condition in the while loop will be false
            if(userChoice.equalsIgnoreCase("Quit")){
              System.out.println("---------------------------------------------------------------------------------------------\n");
              System.out.println("Closing Spotbox....");
              System.out.println("Spotbox has been closed!");
              System.out.println("\n---------------------------------------------------------------------------------------------");
            }

        //If the user chooses Genre, the following code will run 
        } else if(exploreAlbums.equalsIgnoreCase("Genre")){

          //Prompts user with options 
          System.out.println("How many albums would you like to view in this genre?:");
          System.out.println("-All(Enter " + genreLength +")");
          System.out.println("-5");
          System.out.println("-10");
          System.out.println("-15");
          System.out.println("-20");
          System.out.println("---------------------------------------------------------------------------------------------");

          //Prompts user to choose an option
          System.out.print("Please choose one of the given options: ");
          
          // Takes user input
          numberView = input.nextInt();

          // Custom method will check if the user input is valid in relation to the numbers given
          while (numberView != genreLength && numberView != 5 && 
            numberView != 10 && numberView != 15 && numberView!= 20 && numberView!=genreLength) {
              
              //Displays error message, prompts and takes new user input
              System.out.print("That is an invalid option, please try again!: ");
              numberView = input.nextInt();
      
          }
          
          //Reset input
          input.nextLine();

          //Print the albums within the genre 
          System.out.println("---------------------------------------------------------------------------------------------\n");
          System.out.println(mySpotbox.getAlbums(userGenre, "", numberView, exploreAlbums));
          System.out.println("---------------------------------------------------------------------------------------------");
          
          //Asks user if they would like to continue using Spotbox or quit 
          System.out.println("Would you like to use Spotbox again?");
          System.out.print("Enter Continue or Quit: ");

          //Takes user input
          userChoice = input.nextLine();

          //Checks if user input is valid or not
          while (!mySpotbox.checkValid(userChoice, validExplore)){

              //Displays error message, prompts and takes new user input
              System.out.print("That is an invalid option, please try again!: ");
              userChoice = input.nextLine();
          }

          //If the user enters quit, the program will display and an exit message and the condition in the while loop will be false
          if(userChoice.equalsIgnoreCase("Quit")){
            System.out.println("---------------------------------------------------------------------------------------------\n");
            System.out.println("Closing Spotbox....");
            System.out.println("Spotbox has been closed!");
            System.out.println("\n---------------------------------------------------------------------------------------------");
          }
        }

        //If the user enters quit, the program will display and an exit message and the condition in the while loop will be false
        } else if(exploreArtists.equalsIgnoreCase("Quit")){
          userChoice = "Quit";
          System.out.println("Thank you for using Spotbox!");
          System.out.println("---------------------------------------------------------------------------------------------\n");
          System.out.println("Closing Spotbox....");
          System.out.println("Spotbox has been closed!");
          System.out.println("\n---------------------------------------------------------------------------------------------");
        }

      //The code that will execute if the user would like to quit Spotbox
      } else if(userChoice.equalsIgnoreCase("Create")){
        System.out.print("Alright, lets get to making your playlist!(Press ENTER to continue): ");
        input.nextLine();
        System.out.println("\n---------------------------------------------------------------------------------------------");
        System.out.print("What would you like to name your playlist?: ");
        String myPlaylistName = input.nextLine();
        mySpotbox.setPlaylistName(myPlaylistName);
        input.nextLine();
        System.out.println("You have named your playlist" + mySpotbox.getPlaylistName());
        System.out.println("\n---------------------------------------------------------------------------------------------");
        System.out.println("Now lets choose some albums for your playlist!");
        System.out.println("These are the genres you have to choose from");
        for (String genre: mySpotbox.GENRE_LIST){
          System.out.println("-"+genre);
        }
        System.out.println("---------------------------------------------------------------------------------------------");
        System.out.print("Please choose one of the genres listed: ");


      } else if (userChoice.equalsIgnoreCase("Quit")){
        System.out.println("---------------------------------------------------------------------------------------------\n");
        System.out.println("Closing Spotbox....");
        System.out.println("Spotbox has been closed!");
        System.out.println("\n---------------------------------------------------------------------------------------------");
      }
    }

    //Close scanner object input
    input.close();
  }
}