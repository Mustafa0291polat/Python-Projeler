name = input("File name:").strip().lower()
if ".gif" in name:
    print("image/gif")
elif ".jpg" in name:
    print("image/jpeg")
elif "jpeg" in name:
    print("image/jpeg")
elif ".pdf"  in name:
    print("application/pdf")
elif ".png" in name:
    print("image/png")
elif ".txt" in name:
    print("text/plain")
elif ".zip" in name:
    print("application/zip")
else:
   print("application/octet-stream ")
