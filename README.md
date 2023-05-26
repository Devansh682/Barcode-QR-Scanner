# Barcode-QR-Scanner 

This is a Python script that uses OpenCV, Pyzbar, and webbrowser libraries to capture an image through a webcam and decode any QR code or barcode present in the image. If the decoded data is present in a pre-defined list of authorized individuals, the script logs the data and time in a CSV file, marks the code as authorized, and opens the associated website in a new tab(if any). 

## Dependencies

- Python 3.x
- OpenCV (`cv2`)
- Pyzbar (`pyzbar`)
- Numpy (`numpy`)

You can install these dependencies using `pip`:

```bash
pip install opencv-python pyzbar numpy
```

## Usage

1. Clone the repository: `git clone https://github.com/yourusername/QR-Code-Scanner-and-Website-Launcher.git`
2. Navigate to the cloned directory: `cd Barcode-QR-Scanner`
3. Run the script: `index.py`
4. Point your webcam at a QR code or barcode
5. If the qr code is authorized, it will be marked by green boundary - else - by a red boundary
6. If the qr code is authorized and has a website encoded to it,the associated website will be launched in a new tab.

## Customization

You can customize the script by modifying the following things :

- `myDataList`: The list of authorized individuals. You can add or remove entries to this list by modifying the `mydata.txt` file.
- `log.csv`: The name of the CSV file used to log authorized codes and their time of detection.
- `cap.set()`: The dimensions of the webcam capture. You can adjust this to match your webcam's resolution.
- `time.sleep()`: The delay in seconds before opening a website. You can adjust this to prevent multiple QR codes from opening multiple tabs.


## Result
![SS2 ](https://user-images.githubusercontent.com/111366687/236534643-2a47965c-50a5-49db-a4cf-88a04914a8d7.png)



