import { useState } from "react";
import axios from "axios";
import { Button, Input, Card, CardContent } from "@/components/ui";

export default function AIAvatarApp() {
  const [inputText, setInputText] = useState("");
  const [response, setResponse] = useState("");
  const [image, setImage] = useState(null);
  const [video, setVideo] = useState(null);
  const [lipSync, setLipSync] = useState(null);
  const [todoList, setTodoList] = useState([]);
  const [appointments, setAppointments] = useState([]);

  const handleChat = async () => {
    const res = await axios.post("http://localhost:8000/chat", { message: inputText });
    setResponse(res.data.response);
  };

  const handleImageGeneration = async () => {
    const res = await axios.post("http://localhost:8000/image", { prompt: inputText });
    setImage(res.data.file);
  };

  const handleVideoGeneration = async () => {
    const res = await axios.post("http://localhost:8000/video", { prompt: inputText });
    setVideo(res.data.file);
  };

  const handleLipSync = async () => {
    const res = await axios.post("http://localhost:8000/avatar/lipsync", { audio_file: "audio.mp3", avatar_image: "avatar.png" });
    setLipSync(res.data.file);
  };

  const fetchTodos = async () => {
    const res = await axios.get("http://localhost:8000/scheduler/todo/list");
    setTodoList(res.data.todos);
  };

  const fetchAppointments = async () => {
    const res = await axios.get("http://localhost:8000/scheduler/appointment/list");
    setAppointments(res.data.appointments);
  };

  return (
    <div className="p-6 max-w-xl mx-auto space-y-4">
      <Card>
        <CardContent>
          <Input
            type="text"
            placeholder="Enter text or prompt..."
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
          />
          <div className="flex space-x-2 mt-4">
            <Button onClick={handleChat}>Chat</Button>
            <Button onClick={handleImageGeneration}>Generate Image</Button>
            <Button onClick={handleVideoGeneration}>Generate Video</Button>
            <Button onClick={handleLipSync}>Lip Sync</Button>
            <Button onClick={fetchTodos}>View To-Dos</Button>
            <Button onClick={fetchAppointments}>View Appointments</Button>
          </div>
        </CardContent>
      </Card>

      {response && <Card><CardContent><p>{response}</p></CardContent></Card>}
      {image && <img src={`http://localhost:8000/${image}`} alt="Generated" className="w-full" />}
      {video && <video controls className="w-full"><source src={`http://localhost:8000/${video}`} type="video/mp4" /></video>}
      {lipSync && <video controls className="w-full"><source src={`http://localhost:8000/${lipSync}`} type="video/mp4" /></video>}
      
      <Card>
        <CardContent>
          <h2>To-Do List</h2>
          <ul>{todoList.map((todo, index) => (<li key={index}>{todo.task} - {todo.due_date}</li>))}</ul>
        </CardContent>
      </Card>
      
      <Card>
        <CardContent>
          <h2>Appointments</h2>
          <ul>{appointments.map((appt, index) => (<li key={index}>{appt.title} - {appt.date} {appt.time}</li>))}</ul>
        </CardContent>
      </Card>
    </div>
  );
}
