import os
import paramiko


def download_images_from_file(file_path, remote_server, remote_username, remote_password, remote_image_folder):
    # 读取图片名称文件
    with open(file_path, 'r') as file:
        # 逐行读取图片名称
        image_names = [line.strip() for line in file]

    # 创建保存下载图片的文件夹
    local_folder = 'D://downloaded_images'
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)

    # 使用paramiko连接远程服务器
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 使用密钥进行连接（如果使用密码，可以添加 password 参数）
        ssh.connect(remote_server, username=remote_username, password=remote_password)

        # 循环下载图片
        for image_name in image_names:
            remote_image_path = os.path.join(remote_image_folder, image_name)
            local_image_path = os.path.join(local_folder, image_name)

            print(remote_image_path)
            # 创建本地图片所在目录
            local_image_dir = os.path.dirname(local_image_path)
            if not os.path.exists(local_image_dir):
                os.makedirs(local_image_dir)
            # 下载文件
            ftp = ssh.open_sftp()
            ftp.get(remote_image_path, local_image_path)
            ftp.close()

        print("Download completed.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        ssh.close()


if __name__ == "__main__":
    # 替换为实际的文件路径和远程服务器信息
    file_path = 'D://vion//store//staffFeature.txt'
    remote_server = '127.0.0.1'
    remote_username = 'root'
    remote_password = 'root'
    remote_image_folder = '/data/'

    download_images_from_file(file_path, remote_server, remote_username, remote_password, remote_image_folder)
