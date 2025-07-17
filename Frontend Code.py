// Subscribe function to integrate with API Gateway and Lambda for SNS subscription
async function subscribeToEvents() {
    const email = prompt("Enter your email to subscribe to event notifications:");
    if (email) {
        try {
            const response = await fetch('<YOUR_SUBSCRIBE_API_ENDPOINT>', { // Replace with actual endpoint
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email: email })
            });

            const data = await response.json();
            console.log("API Response:", data);

            if (response.ok) {
                alert(data.message); // Display success message from Lambda
            } else {
                alert("Subscription failed. Please try again.");
                console.error(data);
            }
        } catch (error) {
            alert("Error subscribing to events. Please try again later.");
            console.error("Error:", error);
        }
    } else {
        alert("Email is required for subscription.");
    }
}

// Function to submit a new event
async function submitNewEvent(event) {
    event.preventDefault();

    const title = document.getElementById("event-title").value;
    const date = document.getElementById("event-date").value;
    const description = document.getElementById("event-description").value;

    const newEvent = {
        title: title,
        date: date,
        description: description
    };

    try {
        const response = await fetch('<YOUR_CREATE_EVENT_API_ENDPOINT>', { // Replace with actual endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newEvent)
        });

        const result = await response.json();

        if (response.ok) {
            alert("New event created successfully!");
            loadEvents();  // Reload events after creating a new one
        } else {
            alert("Failed to create new event.");
            console.error(result);
        }
    } catch (error) {
        alert("Error creating new event. Please try again.");
        console.error("Error:", error);
    }
}
