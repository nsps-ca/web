function findSizes(imgFile) {
    const newImage = new Image();
    console.log(`💡 Finding sizes for file: ${formatBytes(imgFile.size)}`);
    return new Promise((resolve, reject) => {
        newImage.src = URL.createObjectURL(imgFile);
        newImage.decode().then(() => {
            resolve({
                'width': newImage.width,
                'height': newImage.height
            });
        }).catch((error) => {
            console.error(`💔 Error finding sizes for file: ${formatBytes(imgFile.size)}. Error: ${error}`);
            reject(error);
        });
    })
};

function formatBytes(bytes, decimals = 2) {
    if (!+bytes) return '0 Bytes'
    const k = 1000
    const dm = decimals < 0 ? 0 : decimals
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    const i = Math.floor(Math.log(bytes) / Math.log(k))
    return `${parseFloat((bytes / Math.pow(k, i)).toFixed(dm))} ${sizes[i]}`
}

function getUploadContainer(current) {
    for (let x = 0; x < 10; x++) {
        current = current.parentElement;
        if (current.classList.contains("upload-container")) {
            upload_container = current;
            break;
        }
    }
    return upload_container;
}

function getClosest(className, upload_container) {
    return upload_container.getElementsByClassName(className)[0];
}

function handleFile(file, element) {
    let resetImg = document.querySelector(".card-img-top").src;
    let upload_container = getUploadContainer(element);

    const elements = {
        "card-img-top": getClosest("card-img-top", upload_container),
        "dnd-height": getClosest("dnd-height", upload_container),
        "dnd-width": getClosest("dnd-width", upload_container),
        "dnd-size": getClosest("dnd-size", upload_container),
        "dnd-type": getClosest("dnd-type", upload_container),
        "size-status": getClosest("size-status", upload_container),
        "type-status": getClosest("type-status", upload_container),
        "dimensions-status": getClosest("dimensions-status", upload_container),
        "dnd-target": getClosest("dnd-target", upload_container),
    }

    function resetForm() {
        elements["card-img-top"].src = resetImg;
        elements["dnd-height"].value = "";
        elements["dnd-width"].value = "";
        elements["dnd-size"].value = 0;
        elements["dnd-type"].value = "";
        elements["dnd-target"].classList.remove("bg-primary-subtle");
    }

    findSizes(file).then((sizes) => {
        elements["card-img-top"].src = URL.createObjectURL(file);

        let good = true;
        if (sizes.width > 1400 || sizes.height > 1400) {
            good = false;
            elements["dimensions-status"].innerText = `💔 Max 1920 pixels width or height`;
        } else {
            elements["dimensions-status"].innerText = `✅ Good`;
            elements["dnd-height"].value = sizes.height;
            elements["dnd-width"].value = sizes.width
        }

        if (file.size > 2 * 1024 * 1024) {
            good = false;
            elements["size-status"].innerText = `💔 File size is larger than 2MB`;
        } else {
            elements["size-status"].innerText = `✅ Size`;
            elements["dnd-size"].value = file.size;
        }

        if (file.type !== "image/jpeg") {
            good = false;
            elements["type-status"].innerText = `💔 File type is not JPEG`;
        } else {
            elements["type-status"].innerText = `✅ Type`;
            elements["dnd-type"].value = file.type;
        }

        if (!good) {
            resetForm();
            return;
        }
    }).catch((error) => {
        elements["type-status"].innerText = `💔 Not an image file.`;
        resetForm();
    })
};

window.addEventListener("load", () => {
    const dnd = document.querySelectorAll(".dnd-target");
    for (let element of dnd) {
        element.addEventListener("drop", async(event) => {
            event.preventDefault();

            if (event.dataTransfer.items.length > 1) {
                return;
            }
            const img = event.dataTransfer.items[0];
            handleFile(img.getAsFile(), element);
        })

        element.addEventListener("dragover", async(event) => {
            element.classList.add("bg-primary-subtle");
            event.preventDefault();
        });

        element.addEventListener("dragleave", async(event) => {
            element.classList.remove("bg-primary-subtle");
        });
    }

    const dndLinks = document.querySelectorAll(".dnd-select-link");

    dndLinks.forEach((link) => {
        link.addEventListener("click", (event) => {
            event.preventDefault();
            let upload_container = getUploadContainer(event.target);
            getClosest("dnd-select", upload_container).click();
        });
    });

    const dndSelect = document.querySelectorAll(".dnd-select");

    dndSelect.forEach((input) => {
        input.addEventListener("change", (event) => {
            event.preventDefault();
            const file = event.target.files[0];
            if (file) {
                handleFile(file, event.target);
            }
        })
    })
});