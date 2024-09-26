/*
 * Processes and analyzes data about music
 * This class contains the main methods which will access data from the text files 
 * These methods are used throughout the code to effects user paths and values printed 
 */

 //No parameter constructor, creating class and instantiating varriables/attrtibutes
public class Spotbox {
  private String[] genres;
  private String[] artists;
  private String[] albums;
  private String playlistName;

  //Creates specified array of the genres within genres text file
  public final String[] GENRE_LIST = {"Rock", "Pop", "Blues", 
                                     "Jazz", "Folk", "Country", 
                                     "Reggae", "Classical", "Hip Hop", 
                                     "Stage & Screen", "Funk", "Electronic"};

  //Parameterized constructor
  public Spotbox (String[] genres, String[] artists, String[] albums, String playlistName){
    this.genres = genres;
    this.artists = artists;
    this.albums = albums;
    this.playlistName = playlistName;
  }
  
  /*
   * Accessor method, findsthe ammount of the inputed genre within the genre text file
   * every instance where searchGenre equals the element, counter is increased by one 
   */

  public void setPlaylistName(String playlistName){
    this.playlistName = playlistName;
  }

  public String getPlaylistName(){
    return playlistName;
  }
  
  public int getGenreCount(String searchGenre){
    int count = 0;
    for (String genre:genres){
      if(genre.equalsIgnoreCase(searchGenre)||genre.toLowerCase().contains(searchGenre.toLowerCase())){
        count++;
      }
    }
    return count;
  }

  /*
   * Accessor method, finds the aammount of artists within a genre 
   * every instance where searchArtist equals the element, counter is increased by one 
   */
  public int getArtistCount(String searchArtist){
    int count = 0;
    for(String artist:artists){
      if(artist.equalsIgnoreCase(searchArtist)||artist.toLowerCase().contains(searchArtist.toLowerCase())){
        count++;
      }
    }
    return count;
  } 

  //Checks if user input is valid in relation to the options given
  public boolean checkValid(String genreChoice, String[] list){
    for(String object: list){
      if (object.equalsIgnoreCase(genreChoice)){
        return true;
      }
    }
    return false;
  }

  /*
   * Accessor method, to find albums depending if the user input is genre or artist albums
   * First will create an empty string and counters for possible paths
   * Will check through the genre for index positions
   * If the genre inputed equals to genre element, add album or artist to string 
   */
  public String getAlbums(String searchGenre, String searchArtist, int numberOf, String genreOrArtists){
    String results = "";
    int count = 0;
    int countTwo = 0;
    for (int i = 0; i<genres.length-1;i++){
      if (count >=numberOf||countTwo >= numberOf){
        break;
      }
      if (genreOrArtists.equalsIgnoreCase("Genre")){
        if (genres[i].equalsIgnoreCase(searchGenre)||genres[i].toLowerCase().contains(searchGenre.toLowerCase())){
          results += count+1 + ". " + albums[i] + " by " + artists[i] + "\n";
          count++;

        } 
      } else if(genreOrArtists.equalsIgnoreCase("Artist")){
        if (artists[i].equalsIgnoreCase(searchArtist)||artists[i].toLowerCase().contains(searchArtist.toLowerCase())){
          results += countTwo+1 + ". " + albums[i] + " by " + searchArtist + "\n";
          countTwo++;
        }
      }
    }
    return results;
  }

  /*
   * Accessor method, makes string with the artists within a genre and a given length
   * Checks through if the genre element is equal to genre parameter, then adds artist to the list of that index
   */
  public String[] getArtists(String searchGenre, int numberOf){
    String[] results = new String[numberOf];
    int count = 0;
    for (int i = 0; i<genres.length-1;i++){
      if (count >= numberOf){
        break;
      }
      if (genres[i].equalsIgnoreCase(searchGenre)||genres[i].toLowerCase().contains(searchGenre.toLowerCase())){
        results[count] = artists[i];
        count++;
      }
    }  

  
  return results;
  }
}