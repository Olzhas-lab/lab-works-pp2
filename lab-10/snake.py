import pygame
import random
import psycopg2

# Connect to the database
conn = psycopg2.connect("dbname=snake_db user=postgres password=KeyToLife")
cur = conn.cursor()
# создать таблицу
cur.execute("""
    CREATE TABLE IF NOT EXISTS user_scores (
        username VARCHAR(50) PRIMARY KEY,
        record INT DEFAULT 0
    );
""")
conn.commit()

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display dimensions
dis_width = 600
dis_height = 400

# Set up display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to render score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Function to render personal record
def Your_record(record):
    value = score_font.render("Your Record: " + str(record), True, yellow)
    dis.blit(value, [330, 0])

# Function to draw snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Function to handle game over
def game_over_screen(username):
    dis.fill(blue)
    message("You Lost! Press C-Play Again or Q-Quit", red)
    Your_score(score)
    pygame.display.update()

# Function to pause the game
def pause_game(username):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# Function to save user's record
def save_record(username, record):
    try:
        cur.execute("INSERT INTO user_scores (username, record) VALUES (%s, %s) ON CONFLICT (username) DO UPDATE SET record = EXCLUDED.record", (username, record))
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()  # Rollback transaction in case of error
        print("Error while saving record:", e)

# Function to load user's record
def load_user_record(username):
    cur.execute("SELECT record FROM user_scores WHERE username = %s", (username,))
    existing_user = cur.fetchone()
    if existing_user:
        return existing_user[0]  # Return the user's record
    else:
        cur.execute("INSERT INTO user_scores (username, record) VALUES (%s, %s)", (username, 0))
        conn.commit()
        return 0  # Return zero as the user's record
    
# Function to input name
def get_username_input():
    username = ""
    input_active = True

    input_box = pygame.Rect(150, 180, 300, 40)
    color = pygame.Color('blue')

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

        dis.fill(black)

        # Нарисуем поле и текст
        txt_surface = font_style.render(username, True, white)
        width = max(300, txt_surface.get_width()+10)
        input_box.w = width
        dis.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(dis, color, input_box, 2)

        prompt = font_style.render("Enter your username:", True, white)
        dis.blit(prompt, (180, 130))

        pygame.display.flip()

    return username
def gameLoop():
    global snake_speed
    global score
    game_over = False
    game_close = False

    # Get username from user
    username = get_username_input()


    # Load user's record
    record = load_user_record(username)
    print("Your personal record is:", record)

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Initialize score to zero when the game starts
    score = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Display "Welcome back" message only once at the beginning
    print(f"Welcome back, {username}!")

    while not game_over:
        while game_close:
            game_over_screen(username)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        snake_speed = 15
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:
                    pause_game(username)

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(score)
        Your_record(record)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            random_number = random.randint(1, 3)
            Length_of_snake += random_number
            score += 1

            # Update personal record if the current score is higher
            if score > record:
                record = score
                save_record(username, record)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()