package model;

import java.util.List;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection="video")
public class video {
	
	@Id
	private String id;
	 
	private String video_img;
	 
	private String video_link;
	 
	private List video_urls;
	 
	

	public String getVideo_img() {
		return video_img;
	}

	public void setVideo_img(String video_img) {
		this.video_img = video_img;
	}

	public String getVideo_link() {
		return video_link;
	}

	public void setVideo_link(String video_link) {
		this.video_link = video_link;
	}

	public List getVideo_urls() {
		return video_urls;
	}

	public void setVideo_urls(List video_urls) {
		this.video_urls = video_urls;
	}

	public String getVideo_name() {
		return video_name;
	}

	public void setVideo_name(String video_name) {
		this.video_name = video_name;
	}

	private String video_name;
}
