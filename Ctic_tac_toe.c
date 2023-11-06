#include <stdio.h>
#include <stdbool.h>
#define or ||
#define and &&
#define max 10
#define p(x, ...) printf(x "\n", ##__VA_ARGS__)
#define f false
#define t true
#define gbox char grid_box[][max]

char cha[5] = {'X', 'O'};

char grid_box[max][max] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};

void display_grid(gbox)
{
    for (int i = 0; i < 3; i++)
    {
        printf("   ");

        for (int j = 0; j < 3; j++)
        {
            printf(" %c |", grid_box[i][j]);
        }
        if (i < 2)
            p("\n-------------------");
    }
    p();
}

void winner(char ch)
{
    p("AND the winner is %c", ch);
}

bool horizontal(gbox)
{
    for (int a = 0; a < 3; a++)
    {
        if (grid_box[a][0] != ' ' and (grid_box[a][0] == grid_box[a][1]) and (grid_box[a][0] == grid_box[a][2]))
        {
            winner(grid_box[a][0]);
            return t;
        }
    }
    return f;
}

bool vertical(gbox)
{
    for (int a = 0; a < 3; a++)
    {
        if (grid_box[0][a] != ' ' and (grid_box[0][a] == grid_box[1][a]) and (grid_box[0][a] == grid_box[2][a]))
        {
            winner(grid_box[0][a]);
            return t;
        }
    }
    return f;
}

bool diagonal(gbox)
{
    if ((grid_box[0][0] != ' ' and grid_box[0][0] == grid_box[1][1] and grid_box[0][0] == grid_box[2][2]) or (grid_box[0][2] != ' ' and grid_box[2][0] == grid_box[0][2] and grid_box[2][0] == grid_box[1][1]))
    {
        winner(grid_box[1][1]);
        return t;
    }
    return f;
}

bool state_of(gbox)
{
    return horizontal(grid_box) or vertical(grid_box) or diagonal(grid_box);
}

int main()
{
    display_grid(grid_box);
    int n = 0;
    while (n < 9)
    {
        int indch = cha[n % 2];
        int pos[2];
        p("Enter the position for player %c: i.e 0 1\n", indch);
        scanf("%d%d", &pos[0], &pos[1]);
        fflush(stdin);
        fflush(stdout);
        if (grid_box[pos[0]][pos[1]] == ' ')
        {
            grid_box[pos[0]][pos[1]] = indch;
            n++;
        }
        else
        {
            p("Please enter a valid position!");
        }
        display_grid(grid_box);
        if (n >= 4)
        {
            if (state_of(grid_box))
            {
                break;
            }
        }
    }

    p("\nThank you for playing!");
    return 0;
}