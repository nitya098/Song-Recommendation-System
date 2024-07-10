import express from "express";
import bodyParser from "body-parser";
import axios from "axios";

const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

var tit="Music recommendation"
app.get("/",(req,res)=>{
    res.render("index.ejs",{title:tit});
});

app.post('/recommend', async (req, res) => {
  const song = req.body.song;
  console.log(`Received song: ${song}`);
  try {
      const response = await axios.post('http://127.0.0.1:5000/recommend', { song });
      const recommendations = response.data;
      console.log(`Received recommendations: ${recommendations}`);
      res.render('recommended.ejs', { recommendations });
  } catch (error) {
      console.error('Error fetching recommendations:', error);
      res.status(500).send('Internal Server Error');
  }
});

app.listen(port, () => {
  console.log(`Server running on port ${port}.`);
});