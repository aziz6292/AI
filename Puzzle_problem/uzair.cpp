#include <iostream>
void isnt();
void the();
void moon();
void lovely();
void nelly();
void heart();
int main()
{
    isnt();
    std:: cout<<std::endl;
    the();
    std:: cout<<std::endl;
    moon();
    std:: cout<<std::endl;
    lovely();
    std:: cout<<std::endl;
    nelly();
    std:: cout<<std::endl;
    heart();
    return 0;
}
void isnt()
{
    int rows = 5; // Number of rows in each letter

    // Print each letter using nested loops
    for (int row = 0; row < rows; row++)
    {
        // Print 'I'
        for (int i = 0; i < 5; i++)
        {
            if (row == 0 || row == rows - 1 || i == 2)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'S'
        for (int i = 0; i < 5; i++)
        {
            if ((row == 0 || row == rows - 1) && i != 0 && i != 4)
            {
                std::cout << "*";
            }
            else if (row == 1 && i == 0)
            {
                std::cout << "*";
            }
            else if (row == rows - 2 && i == 4)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'N'
        for (int i = 0; i < 5; i++)
        {
            if (i == 0 || i == 4 || i == row)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print '''
        for (int i = 0; i < 5; i++)
        {
            if (i == 0 && row == 0)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'T'
        for (int i = 0; i < 5; i++)
        {
            if (row == 0 || i == 2)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }

        std::cout << std::endl;
    }
}
void the()
{
    int rows = 5; // Number of rows in each letter

    // Print each letter using nested loops
    for (int row = 0; row < rows; row++)
    {
        // Print 'T'
        for (int i = 0; i < 5; i++)
        {
            if (row == 0 || i == 2)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'H'
        for (int i = 0; i < 5; i++)
        {
            if (i == 0 || i == 4 || row == 2)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'E'
        for (int i = 0; i < 5; i++)
        {
            if (row == 0 || row == rows - 1 || i == 0 || i == 2)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }

        std::cout << std::endl;
    }
}
void moon()
{
    int rows = 5; // Number of rows in each letter

    // Print each letter using nested loops
    for (int row = 0; row < rows; row++)
    {
        // Print 'M'
        for (int i = 0; i < 5; i++)
        {
            if (i == 0 || i == 4 || (row == i && i <= 2) || (row + i == 4 && i > 2))
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'O'
        for (int i = 0; i < 5; i++)
        {
            if ((row == 0 || row == rows - 1 || i == 0 || i == 4) && !(row == 0 && (i == 0 || i == 4)) && !(row == rows - 1 && (i == 0 || i == 4)))
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'O'
        for (int i = 0; i < 5; i++)
        {
            if ((row == 0 || row == rows - 1 || i == 0 || i == 4) && !(row == 0 && (i == 0 || i == 4)) && !(row == rows - 1 && (i == 0 || i == 4)))
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'N'
        for (int i = 0; i < 5; i++)
        {
            if (i == 0 || i == 4 || i == row)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }

        std::cout << std::endl;
    }
}
void lovely()
{
    int rows = 5; // Number of rows in each letter

    // Print each letter using nested loops
    for (int row = 0; row < rows; row++)
    {
        // Print 'L'
        for (int i = 0; i < 5; i++)
        {
            if (i == 0 || row == rows - 1)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'O'
        for (int i = 0; i < 5; i++)
        {
            if ((row == 0 || row == rows - 1 || i == 0 || i == 4) && !(row == 0 && (i == 0 || i == 4)) && !(row == rows - 1 && (i == 0 || i == 4)))
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'V'
        for (int i = 0; i < 5; i++)
        {
            if ((row == i && i <= 2) || (row + i == 4 && i > 2))
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'E'
        for (int i = 0; i < 5; i++)
        {
            if (row == 0 || row == rows - 1 || i == 0 || i == 2)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'L'
        for (int i = 0; i < 5; i++)
        {
            if (i == 0 || row == rows - 1)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'Y'
        for (int i = 0; i < 5; i++)
        {
            if ((i == 0 && row <= 2) || (i == 4 && row <= 2) || (row == i && i >= 3))
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }

        std::cout << std::endl;
    }
}
void nelly()
{
    int rows = 5; // Number of rows in each letter

    // Print each letter using nested loops
    for (int row = 0; row < rows; row++)
    {
        // Print 'N'
        for (int i = 0; i < 5; i++)
        {
            if (i == 0 || i == 4 || i == row)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'E'
        for (int i = 0; i < 5; i++)
        {
            if (row == 0 || row == rows - 1 || i == 0 || i == 2)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'L'
        for (int i = 0; i < 5; i++)
        {
            if (i == 0 || row == rows - 1)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'L'
        for (int i = 0; i < 5; i++)
        {
            if (i == 0 || row == rows - 1)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "    "; // Add space between letters

        // Print 'Y'
        for (int i = 0; i < 5; i++)
        {
            if ((i == 0 && row <= 2) || (i == 4 && row <= 2) || (row == i && i >= 3))
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }

        std::cout << std::endl;
    }
}
void heart()
{
    int rows = 10; // Number of rows in the heart shape

    // Upper half of the heart
    for (int i = rows / 2; i <= rows; i += 2)
    {
        for (int j = 1; j < rows - i; j += 2)
        {
            std::cout << " ";
        }

        for (int j = 1; j <= i; j++)
        {
            std::cout << "*";
        }

        for (int j = 1; j <= rows - i; j++)
        {
            std::cout << " ";
        }

        for (int j = 1; j <= i; j++)
        {
            std::cout << "*";
        }

        std::cout << std::endl;
    }

    // Lower half of the heart
    for (int i = rows; i >= 1; i--)
    {
        for (int j = i; j < rows; j++)
        {
            std::cout << " ";
        }

        for (int j = 1; j <= (i * 2) - 1; j++)
        {
            std::cout << "*";
        }

        std::cout << std::endl;
    }
}