package com.example.demo.dao;

import org.springframework.data.mongodb.repository.MongoRepository;
import model.video;

public interface videoInt extends MongoRepository<video,String>{
	
	
}
