import { useState } from "react";
import axios from "axios";
import { Button, Input, Card, CardContent } from "@/components/ui";

export default function AIAvatarApp() {
  const [inputText, setInputText] = useState("");
  const [response, setResponse] = useState("");
  const [image, setImage] = useState(null);
  const [video, setVideo] = useState(null);

  const handleChat = async () => {
    const res = await axios.post("http://localhost:8000/chat", { message: inputText });
    setResponse(res.data.response);
  };

  const handleImageGeneration = async () => {
    const res = await axios.post("http://localhost:8000/generate_image", { prompt: inputText });
    setImage(res.data.file);
  };

  const handleVideoGeneration = async () => {
    const res = await axios.post("http://localhost:8000/generate_video", { prompt: inputText });
    setVideo(res.data.file);
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
          </div>
        </CardContent>
      </Card>

      {response && <Card><CardContent><p>{response}</p></CardContent></Card>}
      {image && <img src={`http://localhost:8000/${image}`} alt="Generated" className="w-full" />}
      {video && <video controls className="w-full"><source src={`http://localhost:8000/${video}`} type="video/mp4" /></video>}
    </div>
  );
}
