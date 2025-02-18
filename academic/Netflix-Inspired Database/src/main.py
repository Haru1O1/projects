import psycopg2
import config
from sshtunnel import SSHTunnelForwarder
from CLI_Handler import CLI_Handler

def main():
    # SSH Tunnel
    with SSHTunnelForwarder(
        (config.SSH_HOST, config.SSH_PORT),
        ssh_username=config.SSH_USER,
        ssh_password=config.SSH_PASSWORD,
        remote_bind_address=(config.DB_HOST, config.DB_PORT),
        local_bind_address=("127.0.0.1", 54321)  # Local port for the tunnel
    ) as tunnel:
        # Connection to PostgreSQL
        connection = psycopg2.connect(
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            host="127.0.0.1",
            port=tunnel.local_bind_port,
            database=config.DB_NAME
        )

        # Cursor object interacts with database
        cursor = connection.cursor()

        CLI = CLI_Handler(cursor)

        valid_login = CLI.Security_Screen()

        if(valid_login == "valid"):
            CLI.Main_Menu()
        
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
