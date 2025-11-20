from museum.artists import get_artworks


def main():
    print("Search the Art Institue of Chicago")
    artwork = input("Arwork:")
    artworks= get_artworks(query = artwork, limit = 3)
    for artwork in artworks:
            print(f"* {artwork}")


            
main()