package com.example.demo.impl;

import java.util.List;

import javax.annotation.Resource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Component;

import com.example.demo.dao.UserInt;

import model.Users;

@Component
public class UserImpl implements UserInt{
	
//	@Resource
//	private MongoRepository mongo;
	@Autowired
    private MongoTemplate mongoTemplate;
	
	

	@Override
	public Users findByname(String name) {
		Query query = new Query(Criteria.where(name).is(name));
		Users user=mongoTemplate.findOne(query, Users.class);
		return user;
	}

	public Object findAll() {
//		List list=mongo.findAll();
		return null;
	}

	public<Users> String Add(Users user) {
		mongoTemplate.save(user);
		return "ok";
	}

	@Override
	public String deleteByName(String id) {
		mongoTemplate.remove(id);
		return "delete";
	}

}
